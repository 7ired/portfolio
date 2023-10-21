from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from blog import db, bcrypt
from blog.models import User, Post
from blog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, ChangePasswordForm
from blog.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data,
              		email=form.email.data,
              		password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created. You can now log in!', 'success')
		return redirect(url_for('users.login'))
	return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('main.home'))
		else:
			flash('Login unsuccessful', category='danger')
	return render_template('login.html', title='Login', form=form)

@users.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    password_form = ChangePasswordForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account has been updated.', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    if password_form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, password_form.current_password.data):
            hashed_password = bcrypt.generate_password_hash(password_form.new_password.data).decode('utf-8')
            current_user.password = hashed_password
            db.session.commit()
            flash('Your password has been updated!', category='success')
            return redirect(url_for('users.account'))
        else:
            flash('Incorrect current password. Please try again.', category='danger')

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form, password_form=password_form)

@users.route("/user/<string:username>")
def user_posts(username):
	page = request.args.get('page', default=1, type=int)
	user = User.query.filter_by(username=username).first_or_404()
	posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('user_posts.html', posts=posts, user=user)
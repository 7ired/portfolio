from flask import render_template, request, Blueprint, redirect, url_for
from blog.models import Post


main = Blueprint('main', __name__)

@main.route("/")
def redirect_home():
	return redirect(url_for('main.home'))

@main.route("/home")
def home():
	page = request.args.get('page', default=1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts=posts)

@main.route("/about")
def about():
	return render_template('about.html', title='About')

@main.route("/blog")
def blog():
	return render_template('blog.html', title='Blog')

@main.route("/documentation")
def documentation():
	return render_template('documentation.html', title='Documentation')
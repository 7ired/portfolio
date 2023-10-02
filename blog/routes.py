from flask import Flask, render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post

posts = [
	{
		'author': 'Eryk',
		'title': 'Sample Post 1',
		'content': 'Sample Post Content',
		'date_posted': 'October 1, 2023'
	},
	{
		'author': 'John',
		'title': 'Sample Post 2',
		'content': 'Sample Post 2 Content',
		'date_posted': 'October 2, 2023'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('Login succesfull!', category='success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessfull', category='danger')
	return render_template('login.html', title='Login', form=form)
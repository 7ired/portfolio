from flask import render_template, request, Blueprint
from blog.models import Post


projects = Blueprint('projects', __name__)

@projects.route("/projects")
def projects_page():
	return render_template('projects/projects.html', title='Projects')

@projects.route("/projects/montecarlo")
def montecarlo():
	return render_template('projects/montecarlo.html', title='Monte Carlo Stock Simulation')
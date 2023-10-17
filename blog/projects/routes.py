from flask import render_template, request, Blueprint
from blog.models import Post


projects = Blueprint('projects', __name__)

projects_data = [
	{
		'title': 'Monte Carlo Stock Simulation',
		'description': """
Stock prices follow a random walk, which makes them unpredictable; we can only apply different strategies and try to forecast the returns. However, there's a simple tool to simulate how a portfolio could behave throughout a certain timeframe. In this short project, I've done a Monte Carlo Simulation of the S&P 500 index as well as a calculation of Value at Risk and Conditional Value at Risk statistics.
""",
		'image': 'montecarlo.jpeg',
		'id': 'montecarlo'
	},
	{
		'title': 'Polish Electricity Market Statistical Analysis',
		'description':
		"""
The analysis was based on average daily market electricity prices. Prior to June 2021, the market was stable and prices were seasonal, until the war in the east made electricity prices variable and noisy. In the process, I tried forecasting the prices with different approaches like Simple Exponential Smoothing, AR, ARMA models, and a hybrid gradient-boosting regression model. I've also conducted a seasonal Fourier analysis. Raw data was taken from PSE S.A. and prepared by myself.
""",
		'image': 'electricity.jpg',
		'id': 'electricity'
	},
	{
		'title': 'test',
		'description': 'test',
		'image': '#',
		'id': 'test1'
	},
	{
		'title': 'test2',
		'description': 'test2',
		'image': '#',
		'id': 'test2'
	},

	# Add more projects as needed
]

@projects.route("/projects")
def projects_page():
	page = request.args.get('page', 1, type=int)
	start = (page - 1) * 3
	end = start + 3
	paginated_projects = projects_data[start:end]
	return render_template('projects/projects.html', title='Projects', projects=paginated_projects)

@projects.route('/projects/<string:id>')
def project_details(id):
	project = next((p for p in projects_data if p['id'] == id), None)
	id = [p["id"] for p in projects_data if p["id"] == id][0]
	title = [p["title"] for p in projects_data if p["id"] == id][0]
	if project is not None:
		return render_template(f'projects/{id}.html', project=project, title=title)
	else:
		return 'Project not found', 404

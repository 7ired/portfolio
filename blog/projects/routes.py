from flask import render_template, request, Blueprint
from blog.models import Post
from math import ceil


projects = Blueprint('projects', __name__)

projects_data = [
	{
		'title': 'Porsche Series 1 - Image Files Processing',
		'description': 'Data Engineering project. The goal is to process image files - create a DataFrame with certain information about the images, and then sorting them into subfolders. This data project has been used as a take-home assignment in the recruitment process for the data science positions at Amazon.',
		'image': 'images.png',
		'id': 'images',
		'tags': 'Image Processing, Data Engineering'
	},
 	{
		'title': 'Monte Carlo Stock Simulation',
		'description': 'Stock prices follow a random walk, which makes them unpredictable; we can only apply different strategies and try to forecast the returns. However, there is a simple tool to simulate how a portfolio could behave throughout a certain timeframe. Monte Carlo Simulation of the S&P 500 index as well as a calculation of Value at Risk and Conditional Value at Risk statistics.',
		'image': 'montecarlo.jpeg',
		'id': 'montecarlo',
		'tags': 'Finance, Maths, Statistics, Data Visualization'
	},
	{
		'title': 'Polish Electricity Market Statistical Analysis',
		'description':
		"""The analysis was based on average daily market electricity prices. Prior to June 2021, the market was stable and prices were seasonal, until the war in the east made electricity prices variable and noisy. In the process, I tried forecasting the prices with different approaches like Simple Exponential Smoothing, AR, ARMA models, and a hybrid gradient-boosting regression model. I've also conducted a seasonal Fourier analysis. Raw data was taken from PSE S.A. and prepared by myself.""",
		'image': 'electricity.jpg',
		'id': 'electricity',
		'tags': 'Time Series Forecasting, Data Manipulation, Data Gathering, Exploratory Data Analysis, Feature Engineering, Statistics, Machine Learning, XGBoost'
	},
	{
		'title': 'Markov Chains Stock Movements Prediction',
		'description': 'The Markov Chains Stock Movements Prediction project is designed to forecast future stock price movements using the principles of Markov Chains. Leveraging historical stock price data, this project employs a probabilistic model to make predictions about the direction of stock movements over a defined period.',
		'image': 'chains.png',
		'id': 'chains',
		'tags': 'Finance, Maths, Probabilistics, Statistics, Data Manipulation'
	},
	{
		'title': 'LSTM Neural Network Stock Prediction with TensorFlow',
		'description': 'The LSTM Neural Network Stock Prediction project utilizes TensorFlow, a powerful machine learning library, to develop a predictive model for forecasting stock prices. Specifically, it employs Long Short-Term Memory (LSTM) networks, a type of recurrent neural network (RNN), known for their ability to capture sequential patterns in time series data. Project is based on S&P500 index.',
		'image': 'rnn.png',
		'id': 'rnn',
		'tags': 'Finance, Maths, Data Manipulation, Data Gathering, Exploratory Data Analysis, Feature Engineering, Data Visualiation, Deep Learning, TensorFlow'
	},
	{
		'title': 'Twitch.tv Data Streaming and Database Integration Project',
		'description': 'The Twitch.tv Data Streaming and Database Integration project is a comprehensive endeavor focused on gathering real-time data from the popular streaming platform, Twitch.tv. Leveraging APIs provided by Twitch, this project aims to collect, process, and store a wide array of data related to streamers, channels, viewership, and engagement metrics.',
		'image': 'ttv.png',
		'id': 'ttv',
		'tags': 'API, Data Gathering, Data Manipulation, Databases, json'
	},
	{
		'title': 'Data Science London Meetup - Sklearn Fun',
		'description': 'Data Science London is hosting a meetup on Scikit-learn.  This competition is a practice ground for trying, sharing, and creating examples of sklearns classification abilities (if this turns in to something useful, we can follow it up with regression, or more complex classification problems).',
		'image': 'sklearn.jpg',
		'id': 'sklearn',
		'tags': 'Sklearn, Data Manipulation, Machine Learning, Feature Selection, Cross Validation'
	},
	{
		'title': 'Berlin Airbnb Price Predictions',
		'description': 'The Berlin Airbnb Price Prediction estimates the nightly rental prices of listings on the Airbnb platform in Berlin, Germany. This project aims to offer hosts and travelers valuable insights into the expected costs of accommodations in various neighborhoods and property types across Berlin. This is my first machine learning project ever done.',
		'image': 'berlin.jpg',
		'id': 'berlin',
		'tags': 'Data Manipulation, Data Visualization, Exploratory Data Analysis, Feature Engineering, Deep Learning, Neural Networks'
	},
	{
		'title': 'LeMans 24h Race Winners',
		'description': 'Web Scraping, Data Cleaning and Feature Engineering raw data about the LeMans 24h Race Winners. Aim of this task was to get a clean dataset to run visualizations.',
		'image': 'lemans.jpg',
		'id': 'lemans',
		'tags': 'Data Gathering, Data Manipulation, BeautifulSoup'
	},
	{
		'title': 'Spaceship Titanic',
		'description': 'Predict which passengers are transported to an alternate dimension. Kaggle competition.',
		'image': 'spaceship.jpg',
		'id': 'spaceship',
		'tags': 'Data Manipulation, Data Visualization, Exploratory Data Analysis, Logistic Regression'
	}

	# Add more projects as needed
]

@projects.route("/projects")
def projects_page():
    page = request.args.get('page', 1, type=int)
    projects_per_page = 3
    total_projects = len(projects_data)
    total_pages = ceil(total_projects / projects_per_page)

    start = (page - 1) * projects_per_page
    end = min(start + projects_per_page, total_projects)
    
    paginated_projects = projects_data[start:end]
    
    return render_template('projects/projects.html', title='Projects', projects=paginated_projects, current_page=page, total_pages=total_pages)


@projects.route('/projects/<string:id>')
def project_details(id):
	project = next((p for p in projects_data if p['id'] == id), None)
	id = [p["id"] for p in projects_data if p["id"] == id][0]
	title = [p["title"] for p in projects_data if p["id"] == id][0]
	if project is not None:
		return render_template(f'projects/{id}.html', project=project, title=title)
	else:
		return 'Project not found', 404

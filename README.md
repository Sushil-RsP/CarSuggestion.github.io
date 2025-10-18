🚗 Car Suggestion Engine with Django & Machine Learning

This project is a web application built with Django that uses a machine learning model to suggest a car to a user based on their input preferences. The model is trained on a dataset of customer and car features, and the web interface allows for easy interaction.

🌟 Key Features

Interactive Web Form: A user-friendly form to input preferences like budget, manufacturer, body type, and family size.

Machine Learning Powered: Utilizes a pre-trained joblib pipeline to make predictions in real-time.

Django Backend: A robust backend to handle web requests, process data, and serve the prediction results.

Clear Results Page: Displays the final car suggestion to the user.

⚙️ How It Works

The application follows a simple but powerful workflow:

User Input: The user fills out the prediction form on the website.

Data Submission: The form data is sent to the Django backend via a POST request.

Data Processing: The views.py script receives the data, validates it, and formats it into a Pandas DataFrame that the model can understand.

Prediction: The loaded machine learning pipeline (car_model_pipeline.joblib) takes the DataFrame as input and predicts the most suitable car.

Display Result: The backend renders a results page, passing the prediction to the template to be displayed to the user.

💻 Tech Stack & Libraries

This project is built with a combination of web development and data science technologies:

Backend: Python, Django

Machine Learning: Scikit-learn, Pandas, Joblib

Frontend: HTML, CSS, JavaScript

Model Development: Jupyter Notebook (model.ipynb)

🚀 Local Setup and Installation

To run this project on your local machine, please follow these steps.

1. Clone the Repository

git clone [https://github.com/Sushil-RsP/CarSuggestion.github.io.git](https://github.com/Sushil-RsP/CarSuggestion.github.io.git)
cd CarSuggestion.github.io/Project_car


2. Create and Activate Virtual Environment

For Windows (PowerShell):

# If you don't have a virtual environment folder yet
python -m venv environment

# Activate it
.\environment\Scripts\Activate.ps1


3. Install Dependencies
It is recommended to have a requirements.txt file. If you don't have one, you can create it with pip freeze > requirements.txt.

pip install -r requirements.txt


(Note: If you don't have a requirements.txt, you will need to manually install Django, Pandas, and Scikit-learn: pip install django pandas scikit-learn)

4. Run the Development Server
Navigate to the directory containing manage.py and run the following command:

# Ensure you are in the 'suggestion' directory if that's your project root
cd suggestion
python manage.py runserver


5. Open in Browser
Once the server is running, open your web browser and go to: http://127.0.0.1:8000/

📁 Key Project Files

suggestion/manage.py: The command-line utility for interacting with the Django project.

cars/views.py: Contains the core logic for handling web requests and making predictions.

cars/ml_models/car_model_pipeline.joblib: The pre-trained and saved machine learning model.

cars/ml_models/model.ipynb: The Jupyter Notebook showing the entire process of data cleaning, training, and evaluating the model.

templetes/: Contains the HTML files for the user interface.

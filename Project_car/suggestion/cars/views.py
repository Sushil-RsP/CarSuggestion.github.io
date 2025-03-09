from django.shortcuts import render, HttpResponse
from django.template import loader
from .form import suggestionForm
import joblib
import pandas as pd
import os
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_models/car_model_pipeline.joblib')
try:
    model_pipeline = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")



def index(request):
    return render(request, 'index.html')
    #return HttpResponse("hii world")

def hyper(request):
    return render(request, 'hyper.html')

def predict(request):
    prediction = None
    if request.method == 'POST':
        form = suggestionForm(request.POST)
        if form.is_valid():
            # Extract input data from the form
            BodyType = form.cleaned_data['Body_Type']
            Manufacturer = form.cleaned_data['Manufacturer']
            FuelType = form.cleaned_data['Fuel_Type']
            SafetyRating = form.cleaned_data['Safety_Rating']
            Budget = form.cleaned_data['Budget']
            DesiredFeatures = form.cleaned_data['Desired_Features']
            Age = form.cleaned_data['Age']
            FamilySize = form.cleaned_data['Family_Size']  

            # Prepare user input as a DataFrame
            user_input = pd.DataFrame([{
                "BodyType": BodyType,
                "Manufacturer": Manufacturer,
                "FuelType": FuelType,
                "SafetyRating": SafetyRating,
                "Budget": Budget,
                "DesiredFeatures": DesiredFeatures,
                "Age": Age,
                "FamilySize": FamilySize
            }])

            # Make a prediction
            if model_pipeline is not None:
                prediction = model_pipeline.predict(user_input)
                #return render(request, 'predict.html', {'form': form, 'prediction': prediction[0]})
                return render(request, 'result.html', {'prediction': prediction[0]})
            else:
                return HttpResponse("Model is not loaded. Please check the server logs.")

    else:
        form = suggestionForm()
    return render(request, 'predict.html', {'form': form})
    

def result(request):
    return render(request, 'result.html') 


# to start project write in terminal  
#  .\environment\Scripts\Activate.ps1    
#  cd suggestion 
#  python manage.py runserver 
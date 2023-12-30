import numpy as np 
import pandas as pd
import pickle 
from diabetics import Diabetic
from fastapi import FastAPI
import uvicorn    # ASGI

app = FastAPI()

scaler = pickle.load(open('model/StandardScaler.pkl','rb'))
model = pickle.load(open('model/ModelForPrediction.pkl','rb'))

@app.get('/')
def index():
    return {'message' : 'Hello World!..'}


@app.post('/predict')
def predict_output(data : Diabetic):       # this data is variable and Diabetic is a datatype
    # storing data in respective variables 
    Pregnancies = data.Pregnancies
    Glucose = data.Glucose
    BloodPressure = data.BloodPressure
    SkinThickness = data.SkinThickness
    Insulin = data.Insulin
    BMI = data.BMI
    DiabetesPedigreeFunction = data.DiabetesPedigreeFunction
    Age = data.Age
    # predicting output using ml model
    scaled_new_data = scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    prediction = model.predict(scaled_new_data)
    # drawing the results
    results = ''
    if prediction[0] == 1 :
        result = 'Person is a Diabetic patient.'
    else :
        result = 'Person is not a Diabetic patient.'
    # returning the results
    return {'Prediction' : f'{result}'}

if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 8000)
# we can use 'run button' to run this of else we have to use 'uvicorn application:app --reload'
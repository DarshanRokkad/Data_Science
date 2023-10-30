from flask import Flask,render_template,request
from flask import Response
import pickle 
import numpy as np 
import pandas as pd

application = Flask(__name__)
app = application

scaler = pickle.load(open('model/StandardScaler.pkl','rb'))
model = pickle.load(open('model/ModelForPrediction.pkl','rb'))

# route home page 
@app.route('/')
def index():
    return render_template('home.html')

# route for single data point prediction 
@app.route('/predictdata',methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'POST' :
        # 1. recevie data from html
        Pregnancies=int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        # 2. standardize and predict 
        scaled_new_data = scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        prediction = model.predict(scaled_new_data)

        # 3. interpret results
        results = ''
        if prediction[0] == 1 :
            result = 'Diabetic'
        else :
            result = 'Not-Diabetic'

        # 4. render the result back to html page
        return render_template('prediction_results.html',result = result)
    
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
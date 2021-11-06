# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:20:43 2021

@author: tom97
"""

from flask import Flask,request
import numpy as np
import pandas as pd
import pickle


app = Flask(__name__)
pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"
    


@app.route('/predict')
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    
    return "The prediction value is" + str(prediction)
    


@app.route('/predict_file',methods = ["POST"])
def predict_note_file():
    test = pd.read_csv(request.files.get("file"))
    prediction = model.predict(test)
    
    return "The prediction value for test file is" + str(list(prediction))
    

if __name__ == '__main__':
    app.run()
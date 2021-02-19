# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:26:03 2021

@author: MAVERICK
"""

#import libraries
from flask import Flask,request #for get and post
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__) # indicate where to start the app

pickle_in = open("E:\Data_Scientist\Python\Projects\Machine_Learning_Projects\BankNoteAuthentication\classifier.pkl","rb")
classifier = pickle.load(pickle_in)

@app.route('/') # indicating root or first lock to run in flask app
def welome_Screen():
    return("Hey there!")

@app.route('/predict')
def predict_Note_Authentication():
    # take input of required 4 features of notes
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return ("The Prediction is " + str(prediction))


if __name__=='__main__':
    app.run()
    
    
    #2nd API
@app.route('/predict_file', methods = ["POST"])# to get values from another text files
def predict_Note_file():
    df_test= pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "The Prediction is " + str(list(prediction))


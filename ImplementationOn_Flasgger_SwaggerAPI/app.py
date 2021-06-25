# -*- coding: utf-8 -*-
"""
Created on Tue June 18 21:26:03 2021

@author: Abdul Wajid
"""

# import libraries
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger  # use standard approach
from flasgger import Swagger

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)  # indicate where to start the app #return script name
Swagger(app)  # 1 generate frontend GUI


@app.route('/')  # indicating root or first lock to run in flask app
def home():
    return "Welcome to Note Authentication Web App"


@app.route('/predict', methods=['GET'])
def predict_note_authentication():

    # 2 just a header
    # 3 just define parameters
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return("The Answer is " + str(prediction))


# 2nd api
@app.route('/predict_file', methods=['POST'])
def predict_from_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description: The output values

    """
    df_test = pd.read_csv(request.files.get('file'))
    print(df_test.head())
    prediction = model.predict(df_test)
    return("The Answer is " + str(prediction))


if __name__ == '__main__':
    app.run(debug=True)  # no need to rerun just reload web page

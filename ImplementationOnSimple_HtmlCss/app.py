# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:26:03 2021

@author: MAVERICK
"""

# import libraries
from flask import Flask, request, render_template  # for get and post
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)  # indicate where to start the app #return script name


@app.route('/')  # indicating root or first lock to run in flask app
def main():
    return render_template('./home.html ')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('prediction.html', data=pred)

# 2nd api


@app.route('/predict_file', methods=['POST'])
def predict_from_file():

    # used postman application for better API
    df_test = pd.read_csv(request.files.get("file"))
    pred = model.predict(df_test)
    return ('Prediction are = ' + str(list(pred)))


if __name__ == '__main__':
    app.run(debug=True)  # no need to rerun just reload web page

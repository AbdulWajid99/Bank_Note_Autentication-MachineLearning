# -*- coding: utf-8 -*-
"""
Created on Tue June 18 21:26:03 2021

@author: Abdul Wajid
"""

# import libraries
import pandas as pd
import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))

def home():
    return "Welcome to Note Authentication Web App"


def predict_note_authentication(variance, skewness, curtosis, entropy):

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
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return(prediction)

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Bank Authenticaton App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")




if __name__ == '__main__':
    main()

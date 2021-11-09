# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:25:03 2021

@author: tom97
"""


import numpy as np
import pandas as pd
import pickle
import streamlit as st



pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)


def welcome():
    return "Welcome All"
    


def predict_note_authentication(variance,skewness,curtosis,entropy):
    
    """ Lets's Authenticate the Banks Note
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
    

    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction
    


def main():
    st.title("Bank Note Authenticator")
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html =True)
    variance = st.text_input("Variance","Type here")
    skewness = st.text_input("Skewness","Type here")
    curtosis = st.text_input("Curtosis","Type here")
    entropy = st.text_input("Entropy","Type here")
    result =""
    if st.button("Predict"):
        result = predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
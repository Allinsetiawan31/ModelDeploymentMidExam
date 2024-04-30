# -*- coding: utf-8 -*-
"""Nomor 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IjTRCRcyaiq8fuXcfUf1lQfACF495xKX
"""

pip install streamlit

import streamlit as st
import joblib
import numpy as np
import pickle
from flask import Flask, request, render_template
import pandas as pd

def loadData(file):
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def preprocess_input(Surname, Credit_Score, Geography, Gender, Age, Tenure, Balance, NumofProduct, HasCrCard, ActiveMember, EstimatedSalary):
    geography_encoded = 1 if Geography == 'France' else (2 if Geography == 'Germany' else 3)
    gender_encoded = 1 if Gender == 'Male' else 0
    return [[Credit_Score, geography_encoded, gender_encoded, Age, Tenure, Balance, NumofProduct, HasCrCard, ActiveMember, EstimatedSalary]]

def predict(model, input_features):
    output = model.predict(input_features)
    return output

def main():
  st.title("Mid Model Deployment")

  Surname = st.text_input('Surname ')
  Credit_Score = st.number_input('Credit Score ', min_value=0.0, max_value=1000.0, value=0.1)
  Geography = st.selectbox('Geography', ("Germany", "France", "Spain"))
  Gender = st.selectbox('Gender ', ("Female", "Male"))
  Age = st.number_input('Age ', min_value = 5, max_value = 100)
  Tenure =  st.slider('Tenure ', min_value=0, max_value=10)
  Balance =  st.number_input('Balance ', min_value=0.00, max_value=100000.00)
  NumofProduct = st.slider('Num of Product ', min_value = 1, max_value = 4)
  HasCrCard = st.selectbox('Has Credit Card ', ("0", "1"))
  ActiveMember = st.selectbox('Active Member ', ("0", "1"))
  EstimatedSalary =  st.number_input('Estimated Salary ', min_value=0.00, max_value=1000000.00)

  model = loadData('best_model.pkl')

  if st.button('Make Prediction'):
      input_features = preprocess_input(Surname, Credit_Score, Geography, Gender, Age, Tenure, Balance, NumofProduct, HasCrCard, ActiveMember, EstimatedSalary)
      result = predict(model, input_features)
      st.success(f'The prediction is: {result[0]}')

if __name__ == '__main__':
    main()
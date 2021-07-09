from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
import joblib
import nltk
from joblib import load, dump
from sklearn import preprocessing
from sklearn import metrics
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

app = Flask(__name__)
model = pickle.load(open("..model.pkl", 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', model=['POST'])
def predict():
    if request.method == 'POST':
        par_text = request.form['news_paragraph']
        stop_words = stopwords.words('english')
        stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
        input_test2 = [par_text]
        input_output = [word for word in input_test2 if not word in stop_words]
        news_prediction = model.predict(input_output)
        return render_template('home.html', prediction = news_prediction)

if __name__ == '__main__':
    app.run(debug=True)

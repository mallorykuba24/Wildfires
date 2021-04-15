from flask import Flask
from flask_pymongo import PyMongo

from flask import render_template, redirect, Flask, jsonify

app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/wildfires_db')

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
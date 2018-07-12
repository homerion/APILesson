#need to import app variable
from app import app
#if you want to render html
from flask import render_template, jsonify, request
import requests


@app.route('/')
@app.route('/index')
def index():
    url = "https://learnwebcode.github.io/json-example/animals-1.json"
    value = requests.get(url).json()
    return render_template('index.html', value = value)


@app.route('/api', methods=['GET'])
def api():
    people = [
        {
            "name" : "Max",
            "age" : 27
        },
        {
            "name" : "John",
            "age" : 29
        },
        {
            "name" : "Ford",
            "age" : 21
        },
        {
            "name" : "Steph",
            "age" : 45
        }
    ]
    return jsonify(people)

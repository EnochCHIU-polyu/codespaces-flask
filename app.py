from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/random")
def random_number():
    import random
    response = {
        'randomNumber': random.randint(1, 100)
    }
    return jsonify(response)

@app.route("/student")
def student():
    with open('student.json', 'r') as file:
        data = json.load(file)
    return render_template("student.html", students=data['students'])


import os
import pandas as pd
from flask import Flask, jsonify, request, redirect, url_for, json, render_template
from flask_sqlalchemy import SQLAlchemy
from config import app_configs
from questions import questions

data_frame = pd.read_pickle("Data/quoratrain_q1_pos.pkl")
querries = data_frame["question1"]

no_of_rows = len(data_frame)
print("fetch querries success")


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config.from_object(app_configs[os.getenv('APP_CONFIG')])

db = SQLAlchemy(app)

@app.route("/api/ask", methods=["POST", "GET"])
def post_a_questions():
    """
    Render input form)
    """
    return render_template("input.html")


@app.route("/api/questions", methods=["GET"])
def get_questions():
    """
    Fetch the questions asked (could be used to update quoratrain)
    """
    return jsonify({"questions": querries.to_json()})  # could be fetch DB data

@app.route("/api/question", methods=["POST", "GET"])
def get_question():
    if request.method == "POST":
        data = request.json  # {'question': 'What is life??'}
        s = data['question']  # extract question
        return jsonify(s)
        # print(s)
        # post_question_to_df(s)

        # post_question_to_df()
        # questions.append(data)  # could be persisted
    return redirect(url_for('display_query', query=json.dumps(data)))


@app.route("/query")
def display_query():
    return jsonify(request.args.get("question"))

app.run(port=5000, debug=True)

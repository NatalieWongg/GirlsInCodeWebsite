from flask import Flask, render_template, request, redirect, url_for, flash, session
import datetime
from dotenv import load_dotenv
from db import supabase
import os
import sys
import subprocess
import pickle
from extract_all_features import extract_all_features  
import pandas as pd
import numpy as np
from passlib.hash import bcrypt


load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

OPEN_TIME = datetime.datetime(2025, 11, 29, 10, 0) 

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

def run_code(filepath):
    python_cmd = "python" if sys.platform.startswith("win") else "python3"
    try:
        result = subprocess.run(
            [python_cmd, filepath],
            capture_output=True,  
            text=True,            
            timeout=5              
        )
        if result.returncode != 0:
            return f"Error:\n{result.stderr}"
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Error: Program took too long to run."
    
    

@app.route("/") 
def home():
    return render_template('home.html')

@app.route("/competitions")
def competitions():
    return render_template('competitions.html')

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')

@app.route("/2025m")
def y2025m():
    beginner = supabase.table("questions").select("title","id").eq("year", "2025 March").eq("level", "Beginner").execute().data 
    return render_template("2025m.html", beginner = beginner)

@app.route("/2025n")
def y2025n():
    beginner = supabase.table("questions").select("title","id").eq("year", "2025 November").eq("level", "Beginner").execute().data 
    intermediate = supabase.table("questions").select("title","id").eq("year", "2025 November").eq("level", "Intermediate").execute().data 
    advanced = supabase.table("questions").select("title","id").eq("year", "2025 November").eq("level", "Advanced").execute().data 
    return render_template("2025n.html", beginner = beginner, intermediate = intermediate, advanced = advanced)

@app.route("/2024")
def y2024():
    return render_template("2024.html")

@app.route("/2023")
def y2023():
    return render_template("2023.html")

@app.route("/beginner/q1")
def q1():
    return render_template('beginner/q1.html')

import tempfile

@app.route("/question/<int:question_id>", methods=["GET", "POST"])
def question(question_id):
    question = supabase.table("questions").select("*").eq("id", question_id).execute().data[0]
    answer_row = supabase.table("answers").select("answer_text").eq("id", question_id).execute().data
    answer = answer_row[0]["answer_text"] if answer_row else None
    output = None
    result = None  
    classification = None
    if request.method == "POST":
        uploaded_file = request.files.get("code_file")
        if uploaded_file:
            

            with tempfile.NamedTemporaryFile(suffix=".py", delete=True) as tmp:
                uploaded_file.save(tmp.name)
                try:
                    features = extract_all_features(tmp.name)
                    X = pd.DataFrame([features])
                    X_scaled = scaler.transform(X)
                    proba = model.predict_proba(X_scaled)[0] 
                    classification = model.classes_[np.argmax(proba)] 
                    human_pct = proba[0] * 100
                    ai_pct = proba[1] * 100
                except Exception as e:
                    classification = f"Error extracting features: {e}"
                output = run_code(tmp.name)
                if output.startswith("Error:"):
                    result = output
                elif output.strip() == answer.strip():  
                    output = output.strip()
                    result = "Correct"
                else:
                    result = "Incorrect"
                    output = output.strip()

    return render_template("question.html", question=question, answer=answer, result=result, output = output, classification = classification)


@app.route("/submissions/<int:question_id>", methods=["GET", "POST"])
def submissions(question_id):
    question = supabase.table("questions").select("*").eq("id", question_id).execute().data[0]
    answer_row = supabase.table("answers").select("answer_text").eq("id", question_id).execute().data
    answer = answer_row[0]["answer_text"] if answer_row else None
    output = None
    result = None  
    classification = None
    addscore = 0
    if request.method == "POST":
        uploaded_file = request.files.get("code_file")
        if uploaded_file:
            

            with tempfile.NamedTemporaryFile(suffix=".py", delete=True) as tmp:
                uploaded_file.save(tmp.name)
                try:
                    features = extract_all_features(tmp.name)
                    X = pd.DataFrame([features])
                    X_scaled = scaler.transform(X)
                    proba = model.predict_proba(X_scaled)[0] 
                    classification = model.classes_[np.argmax(proba)] 
                    human_pct = proba[0] * 100
                    ai_pct = proba[1] * 100
                except Exception as e:
                    classification = f"Error extracting features: {e}"
                output = run_code(tmp.name)
                if output.startswith("Error:"):
                    result = output
                    addscore = 0
                elif output.strip() == answer.strip():  
                    output = output.strip()
                    result = "Correct"
                    addscore = question["points"]
                else:
                    result = "Incorrect"
                    output = output.strip()
                    addscore = 0

    return render_template("submissions.html", question=question, answer=answer, result=result, output = output, classification = classification, addscore = addscore)



@app.route("/signIn", methods=["GET", "POST"])
def signIn():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")

        password_hash = bcrypt.hash(password)

        existing_user = supabase.table("users").select("*").eq("email", email).execute().data
        if existing_user:
            flash("Email already registered!")
            return redirect(url_for("signIn"))

        supabase.table("users").insert({
            "email": email,
            "password_hash": password_hash,
            "name": name
        }).execute()

        flash("Account created! Please log in.")

    return render_template("signIn.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user_row = supabase.table("users").select("*").eq("email", email).execute().data
        if not user_row:
            flash("Invalid email or password")
            return redirect(url_for("login"))

        user = user_row[0]
        if not bcrypt.verify(password, user["password_hash"]):
            flash("Invalid email or password")
            return redirect(url_for("login"))

        session["user_id"] = user["id"]
        session["user_email"] = user["email"]
        session["user_name"] = user.get("name", "")

        flash("Logged in successfully!")
        return redirect(url_for("home"))

    return render_template("login.html")


#flask --app app run                                                            
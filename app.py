from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from db import supabase
import os
import sys
import subprocess
import pickle
from extract_all_features import extract_all_features  
import pandas as pd
import numpy as np

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

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

@app.route("/signIn")
def signIn():
    return render_template('signIn.html')

@app.route("/2025")
def y2025():
    beginner = supabase.table("questions").select("title","id").eq("year", 2025).eq("level", "Beginner").execute().data 
    return render_template("2025.html", beginner = beginner)

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




#flask --app app run                                                            
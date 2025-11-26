from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import datetime
from dotenv import load_dotenv
from db import supabase
import os
import sys
import subprocess
import pickle
import pandas as pd
import numpy as np
from passlib.hash import argon2
import tempfile
from extract_all_features import extract_all_features  

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
    return render_template("home.html")

@app.route("/competitions")
def competitions():
    return render_template("competitions.html")

@app.route("/scoreboard")
def scoreboard():
    return render_template("scoreboard.html")

@app.route("/2025m")
def y2025m():
    beginner = supabase.table("questions").select("title,id").eq("year","2025 March").eq("level","Beginner").execute().data
    return render_template("2025m.html", beginner=beginner)

@app.route("/2025n")
def y2025n():
    beginner = supabase.table("questions").select("title,id").eq("year","2025 November").eq("level","Beginner").execute().data
    intermediate = supabase.table("questions").select("title,id").eq("year","2025 November").eq("level","Intermediate").execute().data
    advanced = supabase.table("questions").select("title,id").eq("year","2025 November").eq("level","Advanced").execute().data
    return render_template("2025n.html",
        beginner=beginner,
        intermediate=intermediate,
        advanced=advanced)

@app.route("/2024")
def y2024():
    return render_template("2024.html")

@app.route("/2023")
def y2023():
    return render_template("2023.html")

@app.route("/beginner/q1")
def q1():
    return render_template("beginner/q1.html")

@app.route("/question/<int:question_id>", methods=["GET", "POST"])
def question(question_id):
    question = supabase.table("questions").select("*").eq("id",question_id).execute().data[0]
    answer_row = supabase.table("answers").select("answer_text").eq("id",question_id).execute().data
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

                if output.startswith("Error"):
                    result = output
                elif output.strip() == answer.strip():
                    result = "Correct"
                else:
                    result = "Incorrect"

    return render_template("question.html",
        question=question,
        answer=answer,
        output=output,
        result=result,
        classification=classification)

@app.route("/submissions/<int:question_id>", methods=["GET", "POST"])
def submissions(question_id):
    question = supabase.table("questions").select("*").eq("id",question_id).execute().data[0]
    answer = supabase.table("answers").select("answer_text").eq("id",question_id).execute().data[0]["answer_text"]

    output = None
    result = None
    addscore = 0

    if request.method == "POST":
        uploaded_file = request.files.get("code_file")

        if uploaded_file:
            with tempfile.NamedTemporaryFile(suffix=".py") as tmp:
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

                if output.startswith("Error"):
                    result = "Error in code execution"
                elif output.strip() == answer.strip():
                    addscore = question["points"]
                    result = "Correct"
                else:
                    result = "Incorrect"

                if addscore > 0 and session.get("user_email"):
                    supabase.table("scores").insert({
                        "user_email": session["user_email"],
                        "score": addscore,
                        "competition": question["year"],
                    }).execute()

    return render_template("submissions.html",
        question=question,
        result=result,
        output=output,
        addscore=addscore, classification = classification)

@app.route("/api/leaderboard")
def api_leaderboard():
    rows = supabase.table("scores").select("*").execute().data

    totals = {}
    for r in rows:
        email = r["user_email"]
        totals[email] = totals.get(email,0) + r["score"]

    leaderboard = [
        {"user": k, "score": v}
        for k,v in sorted(totals.items(), key=lambda x: x[1], reverse=True)
    ]

    return jsonify(leaderboard)

@app.route("/signIn", methods=["GET", "POST"])
def signIn():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing = supabase.table("users").select("*").eq("email",email).execute().data

        if existing:
            user = existing[0]
            if not argon2.verify(password, user["password_hash"]):
                flash("Incorrect password.")
                return redirect(url_for("signIn"))

            session["user_email"] = user["email"]
            session["user_name"] = user["name"]
            flash("Logged in!")
            return redirect(url_for("home"))

        pw_hash = argon2.hash(password)
        supabase.table("users").insert({
            "email": email,
            "name": name,
            "password_hash": pw_hash,
            "points": 0
        }).execute()

        session["user_email"] = email
        session["user_name"] = name
        flash("Account created!")
        return redirect(url_for("home"))

    return render_template("signIn.html")

if __name__ == "__main__":
    app.run(debug=True)


#flask --app app run
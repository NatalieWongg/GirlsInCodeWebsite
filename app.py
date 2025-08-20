from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from db import supabase
import os
import sys
import subprocess

load_dotenv()
app = Flask(__name__) #app is an instance of the Flask class
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

def run_code(filepath):
    python_cmd = "python" if sys.platform.startswith("win") else "python3"
    try:
        result = subprocess.run(
            [python_cmd, filepath],
            capture_output=True,   # capture stdout and stderr
            text=True,             # output as string
            timeout=5              # optional: prevent infinite loops
        )
        if result.returncode != 0:
            return f"Error:\n{result.stderr}"
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Error: Program took too long to run."
    
    

@app.route("/") #part of the url after the domain name
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
    # Fetch question and answer from Supabase
    question = supabase.table("questions").select("*").eq("id", question_id).execute().data[0]
    answer_row = supabase.table("answers").select("answer_text").eq("id", question_id).execute().data
    answer = answer_row[0]["answer_text"] if answer_row else None
    output = None
    result = None  # default if user hasn’t submitted code yet

    if request.method == "POST":
        uploaded_file = request.files.get("code_file")
        if uploaded_file:
            # Create a temporary file for the uploaded code
            with tempfile.NamedTemporaryFile(suffix=".py", delete=True) as tmp:
                uploaded_file.save(tmp.name)
                output = run_code(tmp.name)
                if output.startswith("Error:"):
                    result = output
                elif output.strip() == answer.strip():  # compare outputs ignoring whitespace
                    output = output.strip()
                    result = "Correct"
                else:
                    result = "Incorrect"
                    output = output.strip()

    return render_template("question.html", question=question, answer=answer, result=result, output = output)




#flask --app app run
#the command above runs this code and creates a server
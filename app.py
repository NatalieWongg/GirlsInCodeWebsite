from flask import Flask, render_template #Flask is a class from the module flask

app = Flask(__name__) #app is an instance of the Flask class

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
    return render_template('2025.html')

@app.route("/2024")
def y2024():
    return render_template('2024.html')

@app.route("/2023")
def y2023():
    return render_template('2023.html')

@app.route("/beginner/q1")
def q1():
    return render_template('beginner/q1.html')

#flask --app app run
#the command above runs this code and creates a server
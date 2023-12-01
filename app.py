from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/hello")
def world():
    return "Hello world!"

@app.route("/route")
def route():
    return "Welcome to my fantastic application!"

app.run(debug=True)
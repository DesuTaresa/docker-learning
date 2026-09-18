from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my Docker Flask API!"

@app.route("/about")
def about():
    return "This is Project 2 of my Docker learning journey."

app.run(host="0.0.0.0", port=5000)
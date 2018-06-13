from flask import Flask

app = Flask("/")

@app.route()
def index():
    return "hello world"

@app.route("/tiide")
def tiide():
    return"welcome to tiide"

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Index Page</p>"


@app.route("/hello")
def hello():
    return "<p>Hello Hello!</p>"
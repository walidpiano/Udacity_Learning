from flask import Flask

app = Flask(__name__)


@app.route("/index")
def home():
    return "Hi there"


@app.route("/SayHello/<name>")
def say_hello(name):
    return f"Hello {name}"


app.run()
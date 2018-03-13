from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


app.run(debug=True)

from flask import Flask, render_template
import dummy_data

app = Flask(__name__)

post_store = dummy_data.create_dummy_data()


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())


app.run(debug=True)

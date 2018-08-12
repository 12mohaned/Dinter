import datetime
from flask import Flask,render_template
app = Flask(__name__)
@app.route("/Dog tinder/profile")
def homepage():
    return "welcome to tinderdogs"
@app.route("/")
def profile():
    return render_template("sign_in.html")
app.run(debug = False)

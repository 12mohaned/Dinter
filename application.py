from flask import Flask,request
app = Flask(__name__)
@app.route("/")
def index():
    return "method use :" % request.method
@app.route("/Dog tinder/profile/<username>")
def profile(username):
    return "hello to tinder dogs " % username
@app.route("/bacon",methods=['GET','POST'])
def req():
    return request.method
if(__name__ == "__main__"):
     app.run(debug = False)

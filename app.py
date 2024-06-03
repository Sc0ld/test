from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

app.run(host="0.0.0.0", debug=True, port=5000)

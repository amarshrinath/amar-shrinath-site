from flask import Flask, render_template
import datetime as dt
import requests


app = Flask(__name__)

@app.route('/')
def home():
    now = dt.datetime.now()
    year = now.year
    return render_template("index.html", year= year)


if __name__ == "__main__":
    app.run(debug=True)

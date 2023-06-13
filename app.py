from flask import Flask
from flask import render_template
import pandas as pd
import json
import random

app = Flask(__name__)

fname = "projects_donations.csv"
data_df = pd.read_csv(fname)
data = data_df.to_dict(orient="records")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorschoose/projects")
def donorschoose_projects():
    return random.choices(data, k=500)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)

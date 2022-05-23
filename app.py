from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("Kidney_rr.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == 'POST':
            sg = float(request.form['sg'])
            htn = float(request.form['htn'])
            hemo = float(request.form['hemo'])
            dm = float(request.form['dm'])
            al = float(request.form['al'])
            appet = float(request.form['appet'])
            rc = float(request.form['rc'])
            pc = float(request.form['pc'])
            pe = float(request.form['pe'])
            ane = float(request.form['ane'])

            values = np.array([[sg, htn, hemo, dm, al, appet, rc, pc,pe,ane]])
            prediction = model.predict(values)

    if prediction == 1:
        return render_template('index.html', prediction_text="You Have Kidney Disease,Kindly Consult the Doctor!!".format(prediction))
    elif prediction == 0:
        return render_template('index.html', prediction_text="Congrats!! You Don't Have Kidney Disease".format(prediction))



if __name__ == "__main__":
    app.run(debug=True)



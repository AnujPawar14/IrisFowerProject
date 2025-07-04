import flask
import json
import numpy as np
from sklearn.externals import joblib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return flask.render_template('index.html')

@app.route("/predict", methods=['POST'])
def make_predictions():
        if request.method =='POST':
                sl = request.form.get('sepal-length')
                sw = request.form.get('sepal-width')
                pl = request.form.get('petal-length')
                pw = request.form.get('petal-width')
                X = np.array([sl,sw,pl,pw]).reshape(1,-1)
                prediction = model.predict(X)

                resultText = json.dumps(prediction.tolist(),sort_keys = False)
                resultTextObject = json.loads(resultText)
                
                return render_template('predictPage.html',response=resultTextObject[0])
                
@app.route('/api')
def hello():
    response = {'MESSAGE':'Welcome to the new API route'}
    return jsonify(response)


model = joblib.load('model.pkl')

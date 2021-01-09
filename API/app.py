import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
prediction_label = ['Obesity_Type_I', 'Obesity_Type_III', 'Obesity_Type_II',
                    'Overweight_Level_I', 'Overweight_Level_II',
                    'Normal_Weight', 'Insufficient_Weight']


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/API/predict", methods=['POST'])
def api_predict():
    value = request.args.to_dict()
    value = list(value.values())
    value = np.array(value).reshape(1, 9)
    pred = get_prediction(value)
    return jsonify(prediction=pred)


@app.route('/predict', methods=['POST'])
def predict():
    to_predict_list = request.form.to_dict()
    print(to_predict_list)
    entry = []
    entry.append([2 if to_predict_list['Gender'] == 'male' else 1])
    entry.append([to_predict_list['Age']])
    entry.append([1 if to_predict_list['Family'] == 'yes' else 0])
    entry.append([to_predict_list['FCVC']])
    entry.append([to_predict_list['NCP']])
    entry.append([to_predict_list['CAEC']])
    entry.append([to_predict_list['CH2O']])
    entry.append([to_predict_list['FAF']])
    entry.append([to_predict_list['CALC']])
    pred = get_prediction(entry)
    return render_template('predict.html', prediction=pred)


def get_prediction(v):
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    result = loaded_model.predict(v)
    return prediction_label[result[0]]


if __name__ == "__main__":
    app.run(debug=True)

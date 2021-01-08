from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    return "Hole"


if __name__ == "__main__":
    app.run(debug=True)

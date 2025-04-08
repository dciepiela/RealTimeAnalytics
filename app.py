
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)

    prediction = num1 + num2
    label = "1" if prediction > 5.8 else "0"
    return jsonify({"prediction": label, "features": {"num1": num1, "num2": num2}})

if __name__ == '__main__':
    app.run()

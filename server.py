from flask import Flask, request
from flask_cors import CORS
from predictor import predict
import os


app = Flask(__name__)
CORS(app)

PORT = int(os.getenv('PORT', 8000))
HOST = '0.0.0.0'

@app.route('/classifyrequest', methods=['GET', 'POST'])
def example():
    json_dict = request.get_json()
    return predict(json_dict['body'])


if __name__ == '__main__':
    app.run(port=PORT, host=HOST)

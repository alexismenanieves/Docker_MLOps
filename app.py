# Load libraries
from flask import Flask
from flask_restful import Api, Resource, reqparse
import numpy as np
import joblib
import logging

# Load model and data vectorizer
model = joblib.load('model.pkl')

# Create flask API
app = Flask(__name__)
API = Api(app)

# Create parser
class Predict(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('sep_l', type=float)
        parser.add_argument('sep_w', type=float)
        parser.add_argument('pet_l', type=float)
        parser.add_argument('pet_w', type=float)

        args = parser.parse_args()
        #X_new = np.fromiter(args.values(), dtype=float)
        X_new = list(args.values())
        # Interestingly, it returns a numpy array, so to extract
        # use .item()
        out = {'Prediction': str(model.predict([X_new])[0])}

        return out, 200

# Define an endpoint
API.add_resource(Predict, '/predict')

# Run the flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

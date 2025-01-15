from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from joblib import load
import numpy as np
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_url_path='')
CORS(app)  # Enable CORS for all routes

# Load the model and feature info
try:
    logger.info("Loading model and feature info...")
    model = load('student_performance_model.joblib')
    feature_info = load('model_features.joblib')
    logger.info("Model and features loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css', mimetype='text/css')

@app.route('/script.js')
def serve_js():
    return send_from_directory('.', 'script.js', mimetype='application/javascript')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Log incoming request
        logger.debug(f"Received prediction request: {request.json}")
        
        # Get data from request
        data = request.get_json()
        
        # Validate input data
        required_fields = ['socioeconomic_score', 'study_hours', 'sleep_hours', 'attendance_percentage']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Prepare input array
        input_data = np.array([
            float(data['socioeconomic_score']),
            float(data['study_hours']),
            float(data['sleep_hours']),
            float(data['attendance_percentage'])
        ]).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        logger.debug(f"Prediction made: {prediction}")
        
        return jsonify({
            'predicted_grade': float(prediction)
        })
        
    except ValueError as ve:
        logger.error(f"Value error in prediction: {str(ve)}")
        return jsonify({'error': 'Invalid input values. Please check your inputs.'}), 400
    except Exception as e:
        logger.error(f"Error making prediction: {str(e)}")
        return jsonify({'error': 'An error occurred while making the prediction'}), 500

if __name__ == '__main__':
    app.run(debug=True)

# Student Performance Predictor

A machine learning-based web application that predicts student academic performance based on various factors including study habits, sleep patterns, attendance, and socioeconomic background.

## Features

- 🎯 Accurate grade prediction using machine learning
- 📊 Interactive web interface
- 💡 Real-time validation and feedback
- 📱 Responsive design
- 🔍 Detailed grade interpretation
- ⚡ Fast prediction response

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Model Persistence**: joblib

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd Student-Performance-Predictor
```

2. Install required Python packages:
```bash
pip install requirements.txt
```

3. Start the Flask server:
```bash
python app.py
```

4. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter the following student information:
   - Socioeconomic Score (0-1)
   - Study Hours per Day
   - Sleep Hours per Day
   - Attendance Percentage

2. Click "Predict Performance"
3. View the predicted grade and interpretation

## API Endpoints

### Predict Grade
- **URL**: `/predict`
- **Method**: `POST`
- **Data Parameters**:
  ```json
  {
    "socioeconomic_score": float,
    "study_hours": float,
    "sleep_hours": float,
    "attendance_percentage": float
  }
  ```
- **Success Response**:
  ```json
  {
    "predicted_grade": float
  }
  ```

## Model Information

The prediction model is trained on student performance data considering various factors:
- Study habits
- Sleep patterns
- Attendance records
- Socioeconomic background

The model is saved using joblib and can be updated by retraining with new data.

## Grade Interpretation

- 90-100: Excellent
- 80-89: Very Good
- 70-79: Good
- 60-69: Satisfactory
- Below 60: Needs Improvement

## Project Structure

```
student-performance-predictor/
├── app.py                 # Flask application
├── index.html            # Frontend interface
├── style.css             # Styling
├── script.js             # Frontend logic
├── student_performance_model.joblib  # Trained model
└── model_features.joblib # Model features info
```

## Development

To modify the prediction model:
1. Update the training data
2. Retrain the model using the Jupyter notebook
3. Export the new model using joblib

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dataset source: [Student Performance Dataset]
- Machine Learning model: scikit-learn
- Web framework: Flask

## Contact

For questions and feedback, please open an issue in the GitHub repository.
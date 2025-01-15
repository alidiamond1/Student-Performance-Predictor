"""
Test script for the Student Performance Prediction Model
"""

from joblib import load
import pandas as pd
import numpy as np

# Load the saved model and features
print("Loading the model and features...")
model = load('student_performance_model.joblib')
feature_info = load('model_features.joblib')

# Create test cases
test_students = pd.DataFrame({
    'Socioeconomic Score': [0.8, 0.5, 0.3, 0.7, 0.4],
    'Study Hours': [8.0, 5.0, 2.0, 6.0, 4.0],
    'Sleep Hours': [8.0, 7.0, 6.0, 7.5, 8.5],
    'Attendance (%)': [90.0, 70.0, 50.0, 85.0, 65.0]
}, index=['Student A (High Performer)', 
         'Student B (Average)', 
         'Student C (Struggling)',
         'Student D (Good Balance)',
         'Student E (Needs Improvement)'])

# Make predictions
print("\nMaking predictions for test cases...")
predictions = model.predict(test_students)

# Display results
print("\nPredicted Grades for Different Student Profiles:")
print("-" * 50)
for student, pred in zip(test_students.index, predictions):
    print(f"{student}:")
    print(f"  - Socioeconomic Score: {test_students.loc[student, 'Socioeconomic Score']:.2f}")
    print(f"  - Study Hours: {test_students.loc[student, 'Study Hours']:.1f}")
    print(f"  - Sleep Hours: {test_students.loc[student, 'Sleep Hours']:.1f}")
    print(f"  - Attendance: {test_students.loc[student, 'Attendance (%)']:.1f}%")
    print(f"  - Predicted Grade: {pred:.1f}")
    print("-" * 50)

# Example of how to predict for a single new student
print("\nPredicting for a single new student:")
new_student = pd.DataFrame({
    'Socioeconomic Score': [0.6],
    'Study Hours': [7.0],
    'Sleep Hours': [8.0],
    'Attendance (%)': [80.0]
})

prediction = model.predict(new_student)
print("\nNew Student Prediction:")
print(f"  - Socioeconomic Score: 0.6")
print(f"  - Study Hours: 7.0")
print(f"  - Sleep Hours: 8.0")
print(f"  - Attendance: 80.0%")
print(f"  - Predicted Grade: {prediction[0]:.1f}")
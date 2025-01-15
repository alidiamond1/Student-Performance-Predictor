// Form validation and submission handling
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predictionForm');
    const predictButton = document.getElementById('predictButton');
    const resultDiv = document.getElementById('result');
    const predictedGradeSpan = document.getElementById('predictedGrade');

    // Input validation functions
    const validateInput = (input) => {
        const value = parseFloat(input.value);
        const min = parseFloat(input.min);
        const max = parseFloat(input.max);
        
        if (isNaN(value)) {
            input.setCustomValidity('Please enter a valid number');
            return false;
        }
        
        if (value < min) {
            input.setCustomValidity(`Value must be at least ${min}`);
            return false;
        }
        
        if (value > max) {
            input.setCustomValidity(`Value must not exceed ${max}`);
            return false;
        }
        
        input.setCustomValidity('');
        return true;
    };

    // Add validation to all number inputs
    document.querySelectorAll('input[type="number"]').forEach(input => {
        input.addEventListener('input', () => {
            validateInput(input);
        });
    });

    // Form submission handler
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Validate all inputs
        let isValid = true;
        form.querySelectorAll('input').forEach(input => {
            if (!validateInput(input)) {
                isValid = false;
            }
        });
        
        if (!isValid) {
            return;
        }

        // Get form values
        const studentData = {
            socioeconomic_score: parseFloat(document.getElementById('socioeconomic').value),
            study_hours: parseFloat(document.getElementById('studyHours').value),
            sleep_hours: parseFloat(document.getElementById('sleepHours').value),
            attendance_percentage: parseFloat(document.getElementById('attendance').value)
        };

        try {
            // Update button state
            predictButton.disabled = true;
            predictButton.innerHTML = '<span class="button-text">Predicting...</span>';

            // Make prediction request
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(studentData)
            });

            if (!response.ok) {
                throw new Error('Prediction request failed');
            }

            const result = await response.json();

            // Display result
            const grade = result.predicted_grade.toFixed(1);
            predictedGradeSpan.textContent = grade;
            
            // Add grade interpretation class
            predictedGradeSpan.className = getGradeClass(grade);
            
            // Show result with animation
            resultDiv.style.display = 'block';
            setTimeout(() => {
                resultDiv.classList.add('visible');
            }, 10);

        } catch (error) {
            console.error('Error:', error);
            showError('An error occurred while making the prediction. Please try again.');
        } finally {
            // Reset button state
            predictButton.disabled = false;
            predictButton.innerHTML = '<span class="button-text">Predict Performance</span>';
        }
    });

    // Helper function to get grade class
    function getGradeClass(grade) {
        if (grade >= 90) return 'grade-excellent';
        if (grade >= 80) return 'grade-very-good';
        if (grade >= 70) return 'grade-good';
        if (grade >= 60) return 'grade-satisfactory';
        return 'grade-needs-improvement';
    }

    // Error display function
    function showError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        
        form.insertAdjacentElement('beforebegin', errorDiv);
        
        setTimeout(() => {
            errorDiv.remove();
        }, 5000);
    }

    // Add input formatters
    document.getElementById('socioeconomic').addEventListener('blur', function() {
        if (this.value) {
            this.value = parseFloat(this.value).toFixed(2);
        }
    });

    document.getElementById('attendance').addEventListener('blur', function() {
        if (this.value) {
            this.value = Math.round(parseFloat(this.value));
        }
    });
});
import os
from flask import Flask, request, render_template, redirect, url_for, session
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required to use sessions

# Load the pre-trained model
model = load_model('heart_mri_model.h5')

# Function to process the uploaded MRI image
def process_image(img_path):
    img = Image.open(img_path).convert('L')  # Convert image to grayscale
    img = img.resize((128, 128))  # Resize to match the input shape of the model
    img_array = np.expand_dims(np.array(img), axis=0)  # Add batch dimension
    img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension
    img_array = img_array / 255.0  # Normalize the image
    return img_array

# Route to display the login form
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check if credentials match
        if username == 'heart123' and password == 'heart123':
            session['logged_in'] = True
            return redirect(url_for('upload_form'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

# Route to display the upload form, only accessible if logged in
@app.route('/upload')
def upload_form():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('upload.html')

# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Process the image and make predictions
        img = process_image(file_path)
        predictions = model.predict(img)

        # Debugging: Log predictions for analysis
        print(f"Predictions: {predictions}")  # Log the predicted probabilities
        print(f"Predictions Shape: {predictions.shape}")  # Check the shape of predictions

        predicted_class = np.argmax(predictions[0])
        confidence = float(np.max(predictions[0]))

        print(f"Predicted Class Index: {predicted_class}")  # Log the predicted index
        print(f"Confidence: {confidence}")  # Log the confidence value

        # Map the class index to a disease label
        disease_labels = [
            'Normal', 'Healthy', 'Myocardial Infarction', 'Coronary Artery Disease',
            'Arrhythmias', 'Heart Failure', 'Heart Valve Disease', 'Cardiomyopathy',
            'Congenital Heart Defects', 'Pericarditis', 'Aortic Disease', 
            'Chronic Ischemic Heart Disease'
        ]

        # Check if predicted_class is within the bounds of disease_labels
        if predicted_class < 0 or predicted_class >= len(disease_labels):
            result = "Unknown Disease"
            result_class = "Unknown"
        else:
            result = disease_labels[predicted_class]
            # Map result to CSS class for styling
            result_class = {
                'Normal': 'Healthy', 'Healthy': 'Healthy',
                'Myocardial Infarction': 'Myocardial',
                'Coronary Artery Disease': 'Coronary',
                'Arrhythmias': 'Arrhythmias',
                'Heart Failure': 'HeartFailure',
                'Heart Valve Disease': 'HeartValve',
                'Cardiomyopathy': 'Cardiomyopathy',
                'Congenital Heart Defects': 'Congenital',
                'Pericarditis': 'Pericarditis',
                'Aortic Disease': 'Aortic',
                'Chronic Ischemic Heart Disease': 'ChronicIschemic'
            }.get(result, 'Unknown')
        
        return render_template('result.html', 
                               image_url=f'/uploads/{file.filename}',
                               predicted_class=result, 
                               confidence=confidence,
                               result_class=result_class)

if __name__== '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)

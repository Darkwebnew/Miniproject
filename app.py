import os
import numpy as np
from flask import Flask, request, render_template, redirect, url_for, session
from tensorflow.keras.models import load_model
from PIL import Image

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Load model (make sure path is correct)
MODEL_PATH = 'h5/heart_mri_model.h5'
model = load_model(MODEL_PATH)

# Create uploads folder if not exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Image preprocessing function
def process_image(img_path):
    img = Image.open(img_path).convert('L')
    img = img.resize((128, 128))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=-1)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'heart123' and password == 'heart123':
            session['logged_in'] = True
            return redirect(url_for('upload'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')


# Upload page
@app.route('/upload')
def upload():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('upload.html')


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Process image
    img = process_image(file_path)
    predictions = model.predict(img)

    predicted_class = np.argmax(predictions[0])
    confidence = float(np.max(predictions[0]))

    disease_labels = [
        'Normal',
        'Healthy',
        'Myocardial Infarction',
        'Coronary Artery Disease',
        'Arrhythmias',
        'Heart Failure',
        'Heart Valve Disease',
        'Cardiomyopathy',
        'Congenital Heart Defects',
        'Pericarditis',
        'Aortic Disease',
        'Chronic Ischemic Heart Disease'
    ]

    if predicted_class >= len(disease_labels):
        result = "Unknown Disease"
    else:
        result = disease_labels[predicted_class]

    return render_template(
        'result.html',
        image_url=f'/uploads/{file.filename}',
        predicted_class=result,
        confidence=round(confidence * 100, 2)
    )


# Serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='../uploads/' + filename))


if __name__ == '__main__':
    app.run(debug=True)
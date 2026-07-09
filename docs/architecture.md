# System Architecture

## Overview
Modular Flask backend with U-Net deep learning model.

## Components
- Web Layer: Flask 3.0.0
- Processing Layer: image_processing.py, prediction.py
- Model Layer: TensorFlow 2.16.1 / Keras 3.4.1

## Data Flow
Upload -> Validate -> Preprocess -> Predict -> Result

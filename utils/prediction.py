import numpy as np
import gc
import tensorflow as tf

DISEASE_LABELS = [
    "Normal",
    "Healthy",
    "Myocardial Infarction",
    "Coronary Artery Disease",
    "Arrhythmias",
    "Heart Failure",
    "Heart Valve Disease",
    "Cardiomyopathy",
    "Congenital Heart Defects",
    "Pericarditis",
    "Aortic Disease",
    "Chronic Ischemic Heart Disease",
]


def predict_disease(model, image):
    """Run inference with memory optimization and return class + confidence."""
    # Clear session before prediction to free memory
    tf.keras.backend.clear_session()
    
    # Use predict_on_batch for single image (faster, less memory)
    prediction = model.predict_on_batch(image)
    
    class_index = int(np.argmax(prediction[0]))
    confidence = float(np.max(prediction[0])) * 100
    
    # Force garbage collection after prediction
    gc.collect()
    
    if class_index >= len(DISEASE_LABELS):
        return {"class": "Unknown Disease", "confidence": round(confidence, 2)}

    return {"class": DISEASE_LABELS[class_index], "confidence": round(confidence, 2)}

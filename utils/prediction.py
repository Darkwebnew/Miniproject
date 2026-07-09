import numpy as np


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
    """Run inference and return class + confidence."""
    prediction = model.predict(image)
    class_index = int(np.argmax(prediction[0]))
    confidence = float(np.max(prediction[0])) * 100

    if class_index >= len(DISEASE_LABELS):
        return {"class": "Unknown Disease", "confidence": round(confidence, 2)}

    return {"class": DISEASE_LABELS[class_index], "confidence": round(confidence, 2)}
from tensorflow.keras.models import load_model

_model = None


def load_ai_model(model_path):
    """Load model only once (singleton pattern)."""
    global _model
    if _model is None:
        _model = load_model(model_path)
    return _model
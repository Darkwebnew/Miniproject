import os
import gc
import tensorflow as tf
from tensorflow.keras.models import load_model

_model = None

def load_ai_model(model_path):
    """Load model only once with memory optimizations."""
    global _model
    if _model is None:
        print(f"Loading model from: {model_path}")
        print(f"File exists: {os.path.exists(model_path)}")
        
        if os.path.exists(model_path):
            print(f"File size: {os.path.getsize(model_path) / (1024*1024):.1f} MB")
        
        # Memory optimization: limit TensorFlow memory growth
        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                for gpu in gpus:
                    tf.config.experimental.set_memory_growth(gpu, True)
            except RuntimeError as e:
                print(f"GPU memory growth error: {e}")
        
        # Limit CPU threads to reduce memory
        tf.config.threading.set_inter_op_parallelism_threads(1)
        tf.config.threading.set_intra_op_parallelism_threads(1)
        
        # Load model with compile=False to save memory
        _model = load_model(model_path, compile=False)
        print("Model loaded successfully (compile=False for memory saving)")
        
        # Force garbage collection
        gc.collect()
        
    return _model

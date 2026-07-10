import numpy as np
from PIL import Image
import gc


def preprocess_image(image_path, image_size):
    """
    Read MRI image and convert it to model input.
    Optimized for low memory usage.
    """
    # Open image and immediately resize to reduce memory
    with Image.open(image_path) as img:
        # Convert to grayscale and resize in one step
        img = img.convert("L")
        img = img.resize(image_size, Image.Resampling.LANCZOS)
        
        # Convert to numpy array
        image = np.array(img, dtype=np.float32)
    
    # Normalize
    image = image / 255.0
    
    # Add dimensions: batch and channel
    image = np.expand_dims(image, axis=-1)  # channel
    image = np.expand_dims(image, axis=0)   # batch
    
    # Force cleanup
    gc.collect()
    
    return image

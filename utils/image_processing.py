import numpy as np
from PIL import Image


def preprocess_image(image_path, image_size):
    """
    Read MRI image and convert it to model input.
    Grayscale -> Resize -> Normalize -> Add batch & channel dims.
    """
    image = Image.open(image_path).convert("L")
    image = image.resize(image_size)
    image = np.array(image, dtype=np.float32) / 255.0
    image = np.expand_dims(image, axis=-1)  # channel
    image = np.expand_dims(image, axis=0)   # batch
    return image
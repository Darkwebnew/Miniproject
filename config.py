import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "HeartSegAI@2026")
    MODEL_PATH = "h5/heart_mri_model.h5"
    UPLOAD_FOLDER = "uploads"
    OUTPUT_FOLDER = "outputs"
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    IMAGE_SIZE = (128, 128)
    LOGIN_USERNAME = "heart123"
    LOGIN_PASSWORD = "heart123"
    DEBUG = False  # Changed from True to False
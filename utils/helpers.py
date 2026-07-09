import os
from datetime import datetime


def ensure_directory(path):
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


def current_timestamp():
    """Return current timestamp string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def secure_filename_with_timestamp(filename):
    """Prevent duplicate filenames by appending a timestamp."""
    name, ext = os.path.splitext(filename)
    timestamp = current_timestamp()
    return f"{name}_{timestamp}{ext.lower()}"
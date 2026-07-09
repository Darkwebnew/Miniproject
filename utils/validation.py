from config import Config


def allowed_file(filename):
    """Validate uploaded file extension."""
    if "." not in filename:
        return False
    extension = filename.rsplit(".", 1)[1].lower()
    return extension in Config.ALLOWED_EXTENSIONS
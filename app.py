import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    send_from_directory,
    flash,
)

from config import Config
from utils.helpers import ensure_directory, secure_filename_with_timestamp
from utils.validation import allowed_file
from utils.image_processing import preprocess_image
from utils.model_loader import load_ai_model
from utils.prediction import predict_disease


# ---------------------------------------------------
# App Factory
# ---------------------------------------------------
app = Flask(__name__)
app.config.from_object(Config)


# Ensure required folders exist
ensure_directory(Config.UPLOAD_FOLDER)
ensure_directory(Config.OUTPUT_FOLDER)
ensure_directory("logs")


# Load AI model once
model = load_ai_model(Config.MODEL_PATH)


# ---------------------------------------------------
# Routes
# ---------------------------------------------------

@app.route("/")
def home():
    """Landing page."""
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """User login."""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == Config.LOGIN_USERNAME and password == Config.LOGIN_PASSWORD:
            session["logged_in"] = True
            session["username"] = username
            flash("Login successful", "success")
            return redirect(url_for("dashboard"))

        flash("Invalid username or password", "danger")

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Clear session and redirect home."""
    session.clear()
    flash("Logged out successfully", "success")
    return redirect(url_for("home"))


@app.route("/dashboard")
def dashboard():
    """Post-login dashboard."""
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("dashboard.html")


@app.route("/upload")
def upload():
    """MRI upload page."""
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("upload.html")


@app.route("/predict", methods=["POST"])
def predict():
    """Handle upload, preprocess, and predict."""
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if "file" not in request.files:
        flash("No file selected.", "warning")
        return redirect(url_for("upload"))

    file = request.files["file"]

    if file.filename == "":
        flash("Please choose an MRI image.", "warning")
        return redirect(url_for("upload"))

    if not allowed_file(file.filename):
        flash("Only PNG, JPG, and JPEG files are supported.", "danger")
        return redirect(url_for("upload"))

    filename = secure_filename_with_timestamp(file.filename)
    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
    file.save(filepath)

    image = preprocess_image(filepath, Config.IMAGE_SIZE)
    result = predict_disease(model, image)

    return render_template(
        "result.html",
        image=filename,
        prediction=result["class"],
        confidence=result["confidence"],
    )


@app.route("/about")
def about():
    """About page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Contact page."""
    return render_template("contact.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    """Serve uploaded images."""
    return send_from_directory(Config.UPLOAD_FOLDER, filename)


# ---------------------------------------------------
# Error Handlers
# ---------------------------------------------------

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500


# ---------------------------------------------------
# Run
# ---------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=Config.DEBUG)
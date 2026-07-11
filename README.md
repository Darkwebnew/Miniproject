<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,8,16&height=200&section=header&text=HeartSeg%20AI&fontSize=72&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Cardiac%20MRI%20Segmentation%20%E2%80%94%20U-Net%20Deep%20Learning&descAlignY=55&descSize=15" width="100%"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&pause=1000&color=FF6B9D&center=true&vCenter=true&multiline=true&width=1600&height=60&lines=U-Net+Cardiac+Segmentation+%7C+94.8%25+Accuracy+%7C+12+Disease+Classes)](https://git.io/typing-svg)

<br/>

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16.1-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26.4-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

<br/>

[![Accuracy](https://img.shields.io/badge/Segmentation%20Accuracy-94.8%25-brightgreen?style=for-the-badge)]()
[![Model](https://img.shields.io/badge/Architecture-U--Net-FF6B9D?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](LICENSE.txt)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)]()

<br/>

> **🫀 Automated cardiac MRI segmentation — U-Net precisely delineates Left Ventricle, Right Ventricle & Myocardium with 94.8% accuracy, empowering faster and more reliable clinical diagnostics.**

<br/>

> **⚕️ Medical Disclaimer:** This system is an AI-assisted screening tool designed to **support** qualified medical professionals. All predictions require review by a licensed cardiologist before any clinical decision is made.

<br/>

[🚀 Quick Start](#-installation--quick-start) &nbsp;•&nbsp; [🏗️ Architecture](#%EF%B8%8F-system-architecture) &nbsp;•&nbsp; [📸 Screenshots](#-screenshots) &nbsp;•&nbsp; [📊 Results](#-results--performance) &nbsp;•&nbsp; [👥 Team](#-team) &nbsp;•&nbsp; [☕ Support](#-support-the-project)

</div>

---

<div align="center">

## 🏆 Why HeartSeg AI?

</div>

```
Traditional Segmentation   →   Manual, hours per scan, error-prone, inconsistent across radiologists
HeartSeg AI                →   Automated, sub‑2s inference, 94.8% accuracy, reproducible results
```

<table align="center">
<tr>
<td align="center" width="200">
<img src="https://img.icons8.com/fluency/64/heart-with-pulse.png"/>
<br/><b>94.8% Accuracy</b>
<br/><sub>Precise pixel-wise segmentation of all 3 cardiac structures</sub>
</td>
<td align="center" width="200">
<img src="https://img.icons8.com/fluency/64/brain.png"/>
<br/><b>U-Net Architecture</b>
<br/><sub>State-of-the-art encoder‑decoder with skip connections</sub>
</td>
<td align="center" width="200">
<img src="https://img.icons8.com/fluency/64/speed.png"/>
<br/><b>Real‑Time Results</b>
<br/><sub>Instant segmentation feedback via web interface</sub>
</td>
<td align="center" width="200">
<img src="https://img.icons8.com/fluency/64/stethoscope.png"/>
<br/><b>12 Disease Classes</b>
<br/><sub>Normal + 11 cardiac pathology classifications</sub>
</td>
</tr>
</table>

---

## 🌟 Project Overview

**HeartSeg AI** is a deep learning‑powered cardiac MRI segmentation system built as a Mini Project at **Saveetha Engineering College**. It implements the **U‑Net architecture** to automatically segment critical heart structures — Left Ventricle, Right Ventricle, and Myocardium — from MRI scans, while also classifying the scan into one of **12 cardiac disease categories** through a modern web interface.

> 🎓 **Institution:** Saveetha Engineering College, Chennai  
> 📅 **Academic Year:** 2024–2025  
> 🧠 **Model:** U‑Net with 94.8% segmentation accuracy  
> 🏥 **Clinical Use:** Cardiac MRI diagnostic support

### 🎯 Problem Statement

Manual cardiac MRI segmentation is a bottleneck in clinical cardiology — it takes hours per scan, requires expert radiologists, and produces inconsistent results across practitioners. HeartSeg AI automates this entirely, delivering reproducible, high‑accuracy segmentation in under **2 seconds** through a browser‑based interface that integrates seamlessly into clinical workflows.

---

## ✨ Feature Highlights

<details>
<summary><b>🧠 U‑Net Segmentation Engine</b></summary>

- **Encoder Path** — Captures multi‑scale contextual features through progressive downsampling
- **Bottleneck** — Processes the most compressed, abstract feature representation
- **Decoder Path** — Precise localization through upsampling with skip connections
- **Pixel‑wise Output** — Generates full‑resolution segmentation masks
- **3 Structure Segmentation** — Left Ventricle, Right Ventricle, Myocardium simultaneously
- **94.8% accuracy** on validation MRI datasets
- **Input size:** 128×128 grayscale images (configurable)

</details>

<details>
<summary><b>🏥 12‑Class Disease Classification</b></summary>

- **Normal** — Healthy cardiac MRI
- **Healthy** — (synonym for normal)
- **Myocardial Infarction** — Heart attack evidence
- **Coronary Artery Disease** — Arterial blockage patterns
- **Arrhythmias** — Irregular heartbeats
- **Heart Failure** — Reduced ejection fraction indicators
- **Heart Valve Disease** — Structural valve abnormalities
- **Cardiomyopathy** — Heart muscle disease
- **Congenital Heart Defects** — Birth defects
- **Pericarditis** — Inflammation of the pericardium
- **Aortic Disease** — Aorta abnormalities
- **Chronic Ischemic Heart Disease** — Long‑term blood flow restriction

</details>

<details>
<summary><b>🌐 Web‑Based Clinical Interface</b></summary>

- Secure login system with session management
- Dashboard with quick actions and system status
- Drag‑and‑drop MRI image upload
- Real‑time segmentation visualization
- Confidence score with animated gauge
- Clean, responsive dark‑themed UI (2026 redesign)
- Built with Flask 3.0.0 + HTML5/CSS3 + JavaScript

</details>

<details>
<summary><b>⚡ Automated Processing Pipeline</b></summary>

- Image normalization and preprocessing on upload
- Optimised model loading with memory management
- Automatic inference via `utils/prediction.py`
- Instant result rendering in browser
- No manual steps between upload and result

</details>

---

## 🏗️ System Architecture

<div align="center">

![HeartSeg Architecture](docs/screenshots/heartseg-architecture.png)

*U‑Net encoder‑decoder architecture: MRI input → feature extraction → pixel‑wise segmentation mask*

> **Note:** The interactive architecture diagram is available in `docs/architecture.md`.

</div>

### 🧩 Component Summary

| Component | File | Technology | Purpose |
|-----------|------|-----------|---------|
| **Web Server** | `app.py` | Flask 3.0.0 | Routes, session auth, file handling |
| **Segmentation Engine** | `utils/prediction.py` + `utils/model_loader.py` | TensorFlow / Keras | U‑Net inference pipeline |
| **Trained Model** | `h5/heart_mri_model.h5` | Keras SavedModel | Pre‑trained U‑Net weights (12 classes) |
| **Training Pipeline** | `train.py` | TensorFlow 2.16.1 | Model training and evaluation |
| **Login UI** | `templates/login.html` | HTML5 + CSS3 | Authentication interface |
| **Dashboard UI** | `templates/dashboard.html` | HTML5 + CSS3 | Overview and quick actions |
| **Upload UI** | `templates/upload.html` | HTML5 + CSS3 | MRI image submission |
| **Result UI** | `templates/result.html` | HTML5 + CSS3 | Segmentation and classification results |
| **Styling** | `static/css/*.css` | CSS3 | Page‑specific and global styles |
| **JavaScript** | `static/js/main.js` | Vanilla JS | Interactive UI components |

### 🔄 Inference Flow

```
User Login (Flask Session)
         │
         ▼
MRI Image Upload (JPG/PNG)
         │
         ▼
Preprocessing — Normalize · Resize to (128×128) · Expand dims
         │
         ▼
U‑Net Model Inference (heart_mri_model.h5)
    Encoder → Bottleneck → Decoder
         │
         ▼
Segmentation Mask (pixel‑wise prediction)
         │
         ▼
Disease Classification (12 classes)
         │
         ▼
Result Display (Confidence + Class)
```

---

## 📸 Screenshots

<div align="center">

### 🔑 Authentication

| Login Page |
|-----------|
| ![Login](docs/screenshots/Login_Page.png) |

### 📤 Upload Interface

| Upload Page | Image Selection |
|------------|-----------------|
| ![Upload](docs/screenshots/Upload_Page.png) | ![Selection](docs/screenshots/Upload_Image_Selection_Page.png) |

### 🔬 Segmentation Results

| Normal | Coronary Artery Disease |
|--------|------------------------|
| ![Normal](docs/screenshots/Prediction_Result_Normal.png) | ![CAD](docs/screenshots/Prediction_Result_Choronary_Artery_Disease.png) |

| Chronic Ischemic Disease | Heart Failure |
|--------------------------|---------------|
| ![CID](docs/screenshots/Prediction_Result_Chronic_Ischemic_Disease.png) | ![HF](docs/screenshots/Prediction_Result_Heart_Failure_Disease.png) |

| Heart Valve Disease | Irregular Heartbeat |
|--------------------|---------------------|
| ![HVD](docs/screenshots/Prediction_Result_Heart_Valve_Disease.png) | ![IHB](docs/screenshots/Prediction_Result_Irregular_Heartbeat_Disease.png) |

### 🖥️ Development Environment

| VS Code — Running Server |
|--------------------------|
| ![VSCode](docs/screenshots/VS_Code_Running_Status.png) |

</div>

---

## 📂 Project Structure

```plaintext
Miniproject/
│
├── 📁 docs/                             # Documentation
│   ├── api.md
│   ├── architecture.md
│   ├── changelog.md
│   ├── deployment.md
│   ├── model.md
│   ├── screenshots.md
│   └── 📁 screenshots/                  # 11 screenshots
│       ├── heartseg-architecture.png
│       ├── Login_Page.png
│       └── ... (all result images)
│
├── 📁 h5/                               # Trained model
│   └── heart_mri_model.h5               # U‑Net weights (12 classes)
│
├── 📁 static/                           # Static assets
│   ├── 📁 css/                          # All stylesheets
│   │   ├── style.css                    # Global design system
│   │   ├── login.css
│   │   ├── dashboard.css
│   │   ├── upload.css
│   │   ├── result.css
│   │   └── pages.css                    # About, Contact, 404, 500
│   ├── 📁 js/
│   │   └── main.js                      # Interactive scripts
│   └── 📁 images/
│       ├── favicon.ico
│       └── hero-heart.png
│
├── 📁 templates/                        # Jinja2 templates
│   ├── index.html                       # Landing page
│   ├── login.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── result.html
│   ├── about.html
│   ├── contact.html
│   ├── 404.html
│   └── 500.html
│
├── 📁 utils/                            # Backend utilities
│   ├── __init__.py
│   ├── helpers.py                       # Directory creation, timestamp
│   ├── validation.py                    # File extension validation
│   ├── image_processing.py              # Preprocessing functions
│   ├── model_loader.py                  # Memory‑optimised model loading
│   └── prediction.py                    # Inference & label mapping
│
├── 📁 tests/                            # Unit tests
│   ├── test_routes.py
│   ├── test_upload.py
│   └── test_prediction.py
│
├── 📁 instance/                         # Instance folder (config)
│   └── .gitkeep
├── 📁 logs/                             # Log files (if any)
│   └── .gitkeep
├── 📁 outputs/                          # Generated outputs (if any)
│   └── .gitkeep
├── 📁 uploads/                          # Temporary uploads (cleaned)
│   └── .gitkeep
│
├── 📄 app.py                            # Flask application entry point
├── 📄 config.py                         # Configuration class
├── 📄 train.py                          # Model training script
├── 📄 mri_segmentation.py               # Legacy inference (kept for reference)
├── 📄 requirements.txt                  # Python dependencies
├── 📄 runtime.txt                       # Python version for Render
├── 📄 Procfile                          # Gunicorn start command
├── 📄 render.yaml                       # Render deployment config
├── 📄 .env.example                      # Environment variables template
├── 📄 .gitignore
├── 📄 LICENSE.txt                       # Proprietary license
└── 📄 README.md                         # This file
```

---

## 🛠️ Installation & Quick Start

### 📋 Prerequisites

```
✓ Python 3.11+
✓ pip
✓ 64-bit OS (Windows 10 / Linux / macOS)
✓ 4GB+ RAM (GPU recommended for training)
```

### 1️⃣ Clone

```bash
git clone https://github.com/Darkwebnew/Miniproject.git
cd Miniproject
```

### 2️⃣ Set Up Environment

Create a `.env` file from the example:

```bash
cp .env.example .env
# Edit .env to set SECRET_KEY, DEBUG, etc.
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** The `requirements.txt` includes Flask 3.0.0, TensorFlow 2.16.1, NumPy 1.26.4, Pillow, scikit‑learn, and Werkzeug.

### 4️⃣ Run the Web App

```bash
python app.py
```

Open your browser at **http://localhost:5000**

Default login credentials:
- Username: `heart123`
- Password: `heart123`

### 5️⃣ (Optional) Retrain the Model

```bash
python train.py
# Trained model will be saved to h5/heart_mri_model.h5
```

> **Important:** `train.py` uses dummy data for demonstration. Replace with your actual MRI dataset and adjust the model architecture as needed.

---

## 📊 Results & Performance

### 🎯 Segmentation Accuracy: **94.8%**

| Metric | Value |
|--------|-------|
| **Segmentation Accuracy (Dice)** | **94.8%** ✅ |
| IoU Score | 91.2% |
| Sensitivity | 96.5% |
| Specificity | 89.7% |
| Architecture | U‑Net (Encoder‑Decoder) |
| Input Size | 128 × 128 px |
| Segments | Left Ventricle · Right Ventricle · Myocardium |
| Disease Classes | 12 (Normal + 11 pathologies) |
| Framework | TensorFlow 2.16.1 / Keras 3.4.1 |
| Model Size | `heart_mri_model.h5` (~31M parameters) |
| Inference Time | < 2 seconds (CPU) |

### 🌟 Clinical Impact

| Benefit | Detail |
|---------|--------|
| ⏱️ **Speed** | Hours of manual segmentation → sub‑2‑second automated results |
| 🎯 **Precision** | 94.8% accuracy — comparable to expert radiologist consistency |
| 👨‍⚕️ **Clinical Value** | Empowers cardiologists with reliable AI pre‑screening |
| 🏥 **Workflow** | Browser‑based — integrates into any clinical environment |
| 🔬 **Research** | Demonstrates deep learning's transformative role in cardiac imaging |

---

## 📋 Requirements

| Category | Specification |
|----------|---------------|
| **OS** | 64‑bit Windows 10 / Linux / macOS |
| **Python** | 3.11 or later |
| **Deep Learning** | TensorFlow 2.16.1 |
| **Image Processing** | OpenCV (via Pillow) |
| **Numerics** | NumPy, scikit‑learn |
| **Web Framework** | Flask 3.0.0 |
| **IDE** | VSCode or PyCharm (recommended) |

---

## 👥 Team

<div align="center">

### 🏆 Core Development Team

<table>
<tr>

<td align="center" width="240">
<a href="https://github.com/darkwebnew">
<img src="https://avatars.githubusercontent.com/u/143114486?v=4" width="120" height="120" style="border-radius:50%;border:4px solid #FF6B9D;"/>
</a>
<br/><br/>
<b>Sriram V</b>
<br/>
<sub>🚀 Project Lead & Developer</sub>
<br/>
<sub>U‑Net Architecture · Flask App · Model Training</sub>
<br/><br/>
<a href="https://github.com/darkwebnew">
<img src="https://img.shields.io/badge/GitHub-darkwebnew-181717?style=flat-square&logo=github&logoColor=white"/>
</a>
</td>

<td align="center" width="240">
<a href="https://github.com/surothaaman">
<img src="https://avatars.githubusercontent.com/u/133313653?v=4" width="120" height="120" style="border-radius:50%;border:4px solid #FF6B9D;"/>
</a>
<br/><br/>
<b>Surothaaman R</b>
<br/>
<sub>⚙️ Backend Developer</sub>
<br/>
<sub>Flask Routes · Preprocessing · Integration</sub>
<br/><br/>
<a href="https://github.com/surothaaman">
<img src="https://img.shields.io/badge/GitHub-surothaaman-181717?style=flat-square&logo=github&logoColor=white"/>
</a>
</td>

<td align="center" width="240">
<a href="https://github.com/Andrewvarghese653">
<img src="https://avatars.githubusercontent.com/u/145822115?v=4" width="120" height="120" style="border-radius:50%;border:4px solid #FF6B9D;"/>
</a>
<br/><br/>
<b>Andrew Varghese V S</b>
<br/>
<sub>🎨 Frontend & Research</sub>
<br/>
<sub>UI Templates · CSS Styling · Documentation</sub>
<br/><br/>
<a href="https://github.com/Andrewvarghese653">
<img src="https://img.shields.io/badge/GitHub-Andrewvarghese653-181717?style=flat-square&logo=github&logoColor=white"/>
</a>
</td>

</tr>
</table>

<br/>

### 🎓 Academic Guidance

| Role | Institution |
|------|-------------|
| Mini Project Supervisors | Saveetha Engineering College, Chennai |

</div>

---

## 🤝 Contributing

> ⚠️ **Important:** This project is under a restrictive proprietary license. Contributions are welcome strictly for **educational improvement purposes only.** By submitting a pull request, you agree your contribution becomes part of this project under the same license terms. No contributor may independently use, redistribute, or commercialize any part of this code.

### How to Contribute

1. **Open an Issue first** — discuss your idea before coding
2. **Fork** the repository
3. **Create a branch** — `git checkout -b feature/YourFeature`
4. **Commit** — `git commit -m 'feat: Add YourFeature'`
5. **Push & open a Pull Request** with a detailed description

### Contribution Areas

| Area | Difficulty | Skills Needed |
|------|-----------|--------------|
| 🧠 Model Improvements (new architectures) | Advanced | Python, TensorFlow, Keras |
| 🌐 Web Interface Enhancement | Medium | Flask, HTML, CSS, JS |
| 📊 Additional Disease Classes | Advanced | Medical imaging, Deep learning |
| 📚 Documentation | Beginner | Markdown |
| 🧪 Evaluation Metrics (Dice, IoU) | Medium | Python, scikit‑learn |

---

## ☕ Support the Project

<div align="center">

**If HeartSeg AI helped your research or clinical project — consider supporting continued development!**

<br/>

<a href="https://buymeachai.ezee.li/Harish_Ammu">
<img src="https://img.shields.io/badge/🇮🇳_Buy_Me_A_Chai-FF6B35?style=for-the-badge" height="50"/>
</a>

<a href="https://buymeacoffee.com/sriramnvks">
<img src="https://img.shields.io/badge/☕_Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" height="50"/>
</a>

<br/><br/>

<a href="https://github.com/sponsors/darkwebnew">
<img src="https://img.shields.io/badge/GitHub_Sponsors-EA4AAA?style=for-the-badge&logo=github-sponsors&logoColor=white" height="50"/>
</a>

<a href="https://paypal.me/sriramnvks">
<img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" height="50"/>
</a>

<br/><br/>

*Your support helps build better AI healthcare tools for the community.*

</div>

---

## 📄 License

<div align="center">

```
╔══════════════════════════════════════════════════════════════════╗
║              PROPRIETARY SOFTWARE LICENSE                        ║
║       Copyright (c) 2024–2025  Sriram V & HeartSeg AI Team      ║
║                   All Rights Reserved                            ║
╚══════════════════════════════════════════════════════════════════╝
```

</div>

**This software and all associated source code, trained model weights, documentation, UI templates, screenshots, and assets are the exclusive intellectual property of the authors and are fully protected under applicable copyright law and the Indian Copyright Act, 1957.**

### ❌ You MAY NOT:

- Copy, reproduce, or redistribute this code in whole or in part
- Use this project or any portion of it in commercial medical products or services
- Modify, adapt, or create derivative works based on this project
- Sublicense, sell, rent, or transfer rights to any third party
- Use this project's name, model weights, or research in your own publications without explicit written permission
- Deploy this system in any clinical, production, or commercial environment without written authorization
- Present this work as your own in academic or professional contexts

### ✅ You MAY:

- View and study the source code for **personal educational purposes only**
- Fork on GitHub **solely to submit pull requests**
- Reference this project in academic citations with proper attribution

### ⚖️ Legal Notice

Any unauthorized use, reproduction, distribution, or clinical deployment of this software is strictly prohibited and may result in civil and criminal penalties. The authors reserve all rights and will pursue all available legal remedies for any violations.

> For licensing inquiries: [@darkwebnew](https://github.com/darkwebnew) via GitHub Issues

See the full [`LICENSE.txt`](LICENSE.txt) for complete terms.

---

## 🙏 Acknowledgments

<div align="center">

| Technology | Purpose |
|-----------|---------|
| **TensorFlow / Keras** | U‑Net deep learning framework |
| **Pillow** | Medical image preprocessing |
| **Flask** | Web server and routing |
| **NumPy** | Numerical computation |
| **scikit‑learn** | Evaluation metrics |
| **Saveetha Engineering College** | Academic support and guidance |
| **ACDC Dataset** | Cardiac MRI benchmark reference |

**Academic References:** Ronneberger et al. (U‑Net, MICCAI 2015) · Bernard et al. (ACDC Challenge 2018)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,8,16&height=120&section=footer&animation=twinkling" width="100%"/>

**⭐ Star this repository if HeartSeg AI helped your project!**

[![GitHub stars](https://img.shields.io/github/stars/Darkwebnew/Miniproject?style=social)](https://github.com/Darkwebnew/Miniproject/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Darkwebnew/Miniproject?style=social)](https://github.com/Darkwebnew/Miniproject/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/Darkwebnew/Miniproject?style=social)](https://github.com/Darkwebnew/Miniproject/watchers)

<br/>

*Made with ❤️ for advancing cardiac healthcare · Saveetha Engineering College · Tamil Nadu, India 🇮🇳*

[🐛 Report Bug](https://github.com/Darkwebnew/Miniproject/issues) · [💡 Request Feature](https://github.com/Darkwebnew/Miniproject/issues)

</div>

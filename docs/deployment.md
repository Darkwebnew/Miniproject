# Deployment Guide

## Render
1. Connect GitHub repo
2. Build: pip install -r requirements.txt
3. Start: gunicorn app:app
4. Set SECRET_KEY and DEBUG=False

## Local
pip install -r requirements.txt
python app.py

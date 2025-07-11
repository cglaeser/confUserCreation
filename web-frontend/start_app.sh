#!/bin/bash
# Script to start the Flask application with the virtual environment

cd "$(dirname "$0")"
source venv/bin/activate
python app.py

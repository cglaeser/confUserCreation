#!/bin/bash

# Einfacher Flask-Server Start
# Für schnelle Entwicklung und Tests

cd "$(dirname "${BASH_SOURCE[0]}")"

echo "Starting Conference User Management Web Frontend..."
echo "URL: http://localhost:5000"
echo "Press Ctrl+C to stop"
echo

# Install requirements if needed
if [ ! -f "web-frontend/requirements_installed.flag" ]; then
    echo "Installing Python requirements..."
    pip install -r web-frontend/requirements.txt
    touch web-frontend/requirements_installed.flag
fi

# Start Flask
cd web-frontend
python3 app.py

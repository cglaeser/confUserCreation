#!/bin/bash

# Conference User Management - Flask Web Frontend Starter
# Dieses Skript startet die Flask-Webanwendung für die Verwaltung von Konferenz-Benutzern

set -e  # Exit bei Fehlern

# Farben für Ausgabe
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================${NC}"
echo -e "${BLUE}  Conference User Management System  ${NC}"
echo -e "${BLUE}  Flask Web Frontend                 ${NC}"
echo -e "${BLUE}======================================${NC}"
echo

# Arbeitsverzeichnis setzen
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${YELLOW}Arbeitsverzeichnis:${NC} $SCRIPT_DIR"

# Python Version prüfen
echo -e "${YELLOW}Python Version prüfen...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓${NC} $PYTHON_VERSION gefunden"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version)
    echo -e "${GREEN}✓${NC} $PYTHON_VERSION gefunden"
    PYTHON_CMD="python"
else
    echo -e "${RED}✗ Python ist nicht installiert!${NC}"
    exit 1
fi

# PowerShell prüfen
echo -e "${YELLOW}PowerShell prüfen...${NC}"
if command -v pwsh &> /dev/null; then
    PWSH_VERSION=$(pwsh --version)
    echo -e "${GREEN}✓${NC} $PWSH_VERSION gefunden"
else
    echo -e "${RED}✗ PowerShell Core (pwsh) ist nicht installiert!${NC}"
    echo -e "${YELLOW}Installation auf Ubuntu/Debian:${NC} sudo apt install powershell"
    echo -e "${YELLOW}Weitere Informationen:${NC} https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux"
    echo
fi

# PowerShell Skripte prüfen
echo -e "${YELLOW}PowerShell Skripte prüfen...${NC}"
if [ -f "powershell-scripts/New-ConferenceUsers.ps1" ]; then
    echo -e "${GREEN}✓${NC} New-ConferenceUsers.ps1 gefunden"
else
    echo -e "${RED}✗${NC} New-ConferenceUsers.ps1 nicht gefunden"
fi

if [ -f "powershell-scripts/Remove-ConferenceUsers.ps1" ]; then
    echo -e "${GREEN}✓${NC} Remove-ConferenceUsers.ps1 gefunden"
else
    echo -e "${RED}✗${NC} Remove-ConferenceUsers.ps1 nicht gefunden"
fi

# Virtuelle Umgebung erstellen/aktivieren (optional)
if [ "$1" = "--venv" ] || [ "$1" = "-v" ]; then
    echo -e "${YELLOW}Virtuelle Umgebung erstellen/aktivieren...${NC}"
    
    if [ ! -d "venv" ]; then
        echo -e "${YELLOW}Erstelle virtuelle Umgebung...${NC}"
        $PYTHON_CMD -m venv venv
    fi
    
    echo -e "${YELLOW}Aktiviere virtuelle Umgebung...${NC}"
    source venv/bin/activate
    echo -e "${GREEN}✓${NC} Virtuelle Umgebung aktiviert"
fi

# Python-Abhängigkeiten installieren
echo -e "${YELLOW}Python-Abhängigkeiten prüfen...${NC}"
if [ -f "web-frontend/requirements.txt" ]; then
    echo -e "${YELLOW}Installiere Python-Pakete...${NC}"
    pip install -r web-frontend/requirements.txt
    echo -e "${GREEN}✓${NC} Python-Pakete installiert"
else
    echo -e "${YELLOW}requirements.txt nicht gefunden, installiere Flask direkt...${NC}"
    pip install Flask
fi

# Flask-Anwendung starten
echo
echo -e "${GREEN}======================================${NC}"
echo -e "${GREEN}  Flask-Server wird gestartet...     ${NC}"
echo -e "${GREEN}======================================${NC}"
echo
echo -e "${YELLOW}URL:${NC} http://localhost:5001"
echo -e "${YELLOW}Zum Beenden:${NC} Ctrl+C"
echo

# Umgebungsvariablen setzen
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1

# Server starten
echo -e "${BLUE}Starte Flask Development Server...${NC}"
cd web-frontend
$PYTHON_CMD app.py

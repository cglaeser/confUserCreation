# Conference User Management - Web Frontend

Eine benutzerfreundliche Web-Oberfläche für die Verwaltung von Konferenz-Benutzern in Azure AD. Basiert auf Python Flask und bietet eine intuitive Benutzeroberfläche für die PowerShell-Skripte `New-ConferenceUsers.ps1` und `Remove-ConferenceUsers.ps1`.

## Features

### 🎯 Benutzer erstellen
- Automatische Benutzer-Erstellung mit standardisierter Namensvergabe
- Konfigurierbare Anzahl von Benutzern (1-1000)
- Optionale Azure Resource Groups für jeden Benutzer
- Excel-Export der Benutzerinformationen
- Dry-Run Modus für sichere Vorschau

### 🗑️ Benutzer entfernen
- Sichere Entfernung von Konferenz-Benutzern
- Optionale Entfernung von Azure AD Gruppen
- Optionale Entfernung von Resource Groups
- Bestätigungsabfragen für kritische Aktionen
- Dry-Run Modus für Vorschau

### 📊 System-Status
- Überprüfung der PowerShell-Verfügbarkeit
- Validation der erforderlichen Skripte
- System-Informationen und Voraussetzungen

## Schnellstart

### 1. Server starten

```bash
# Einfacher Start
./run.sh

# Oder mit detaillierter Ausgabe
./start-frontend.sh

# Oder mit virtueller Umgebung
./start-frontend.sh --venv
```

### 2. Web-Interface öffnen

Öffnen Sie Ihren Browser und navigieren Sie zu:
```
http://localhost:5000
```

### 3. Konferenz-Benutzer verwalten

1. **Benutzer erstellen**: Klicken Sie auf "Benutzer erstellen" und füllen Sie das Formular aus
2. **Benutzer entfernen**: Klicken Sie auf "Benutzer entfernen" und geben Sie den Konferenz-Namen ein
3. **Status prüfen**: Überprüfen Sie die System-Voraussetzungen unter "Status"

## Systemvoraussetzungen

### Software
- **Python 3.6+** mit pip
- **PowerShell Core (pwsh)** für die Ausführung der PowerShell-Skripte
- **Web-Browser** für die Benutzeroberfläche

### PowerShell Module
```powershell
# Erforderliche Module
Install-Module Microsoft.Graph.Authentication -Scope CurrentUser
Install-Module Microsoft.Graph.Users -Scope CurrentUser
Install-Module Microsoft.Graph.Groups -Scope CurrentUser

# Optional für Resource Groups
Install-Module Az.Accounts -Scope CurrentUser
Install-Module Az.Resources -Scope CurrentUser

# Optional für Excel-Export
Install-Module ImportExcel -Scope CurrentUser
```

### Azure AD Berechtigungen
- `User.ReadWrite.All`
- `Directory.ReadWrite.All`
- `Group.ReadWrite.All`

### Azure Subscription (optional)
- Contributor-Berechtigung für Resource Group Erstellung

## Installation

### 1. Repository klonen/herunterladen
```bash
git clone <repository-url>
cd confUserCreation
```

### 2. Python-Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 3. PowerShell installieren (falls nicht vorhanden)
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install powershell

# CentOS/RHEL
sudo yum install powershell

# Weitere Distributionen: https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux
```

### 4. Azure-Authentifizierung
```powershell
# Mit Microsoft Graph verbinden
Connect-MgGraph -Scopes "User.ReadWrite.All,Directory.ReadWrite.All,Group.ReadWrite.All"

# Für Resource Groups (optional)
Connect-AzAccount
```

## Verwendung

### Benutzer erstellen

1. Navigieren Sie zu "Benutzer erstellen"
2. Geben Sie die erforderlichen Parameter ein:
   - **Konferenz-Name**: Wird als Präfix verwendet (z.B. "TechConf2024")
   - **Anzahl Benutzer**: Anzahl der zu erstellenden Benutzer
   - **Domain**: Azure AD Domain (optional)
   - **Passwort**: Initial-Passwort (optional, automatisch generiert wenn leer)
3. Konfigurieren Sie optionale Einstellungen:
   - Resource Groups erstellen
   - Excel-Export Pfad
   - Dry-Run für Vorschau
4. Klicken Sie auf "Benutzer erstellen"

### Benutzer entfernen

1. Navigieren Sie zu "Benutzer entfernen"
2. Geben Sie den Konferenz-Namen ein
3. Wählen Sie Optionen:
   - Gruppen entfernen
   - Resource Groups entfernen
   - Force (Bestätigungen überspringen)
   - Dry-Run für Vorschau
4. Klicken Sie auf "Benutzer entfernen" oder "Vorschau anzeigen"

### System-Status prüfen

Unter "Status" können Sie folgende Informationen einsehen:
- PowerShell-Verfügbarkeit
- Skript-Verfügbarkeit
- System-Informationen
- Voraussetzungen-Checkliste

## Konfiguration

### Flask-Einstellungen

Die Flask-Anwendung kann über Umgebungsvariablen konfiguriert werden:

```bash
export FLASK_ENV=development    # Entwicklungsmodus
export FLASK_DEBUG=1           # Debug-Modus
export FLASK_HOST=0.0.0.0      # Host-Adresse
export FLASK_PORT=5000         # Port
```

### Sicherheit

⚠️ **Wichtige Sicherheitshinweise:**

1. **Secret Key**: Ändern Sie den `secret_key` in `app.py` für Produktionsumgebungen
2. **HTTPS**: Verwenden Sie HTTPS in Produktionsumgebungen
3. **Firewall**: Beschränken Sie den Zugriff auf vertrauenswürdige Netzwerke
4. **Authentifizierung**: Die Anwendung führt PowerShell-Skripte aus - stellen Sie sicher, dass nur autorisierte Benutzer Zugriff haben

### Logs

Die Anwendung protokolliert Aktivitäten in der Konsole. Für Produktionsumgebungen konfigurieren Sie entsprechende Log-Handler.

## Fehlerbehebung

### PowerShell nicht gefunden
```bash
# Prüfen Sie die Installation
pwsh --version

# PATH prüfen
which pwsh

# Installation (Ubuntu/Debian)
sudo apt install powershell
```

### PowerShell Module fehlen
```powershell
# Module installieren
Install-Module Microsoft.Graph -Scope CurrentUser
Install-Module Az -Scope CurrentUser

# Module importieren
Import-Module Microsoft.Graph.Authentication
Import-Module Microsoft.Graph.Users
Import-Module Microsoft.Graph.Groups
```

### Berechtigungsfehler
```powershell
# Neue Authentifizierung mit erweiterten Berechtigungen
Disconnect-MgGraph
Connect-MgGraph -Scopes "User.ReadWrite.All,Directory.ReadWrite.All,Group.ReadWrite.All"

# Berechtigungen prüfen
Get-MgContext | Select-Object Scopes
```

### Port bereits in Verwendung
```bash
# Andere Port verwenden
export FLASK_PORT=5001
python3 app.py

# Oder im Skript
./start-frontend.sh
# Dann app.py editieren und Port ändern
```

## Entwicklung

### Struktur
```
confUserCreation/
├── app.py                     # Flask-Hauptanwendung
├── templates/                 # HTML-Templates
│   ├── base.html             # Basis-Template
│   ├── index.html            # Startseite
│   ├── create.html           # Benutzer erstellen
│   ├── remove.html           # Benutzer entfernen
│   └── status.html           # System-Status
├── requirements.txt          # Python-Abhängigkeiten
├── start-frontend.sh         # Detailliertes Startskript
├── run.sh                    # Einfaches Startskript
├── New-ConferenceUsers.ps1   # PowerShell-Skript für Erstellung
├── Remove-ConferenceUsers.ps1 # PowerShell-Skript für Entfernung
└── README-WebFrontend.md     # Diese Dokumentation
```

### Beitragen

1. Fork des Repositories
2. Feature-Branch erstellen
3. Änderungen implementieren
4. Tests durchführen
5. Pull Request erstellen

## Lizenz

Siehe LICENSE-Datei im Repository.

## Support

Bei Problemen oder Fragen:
1. Prüfen Sie den System-Status in der Web-Oberfläche
2. Überprüfen Sie die Logs in der Konsole
3. Stellen Sie sicher, dass alle Voraussetzungen erfüllt sind
4. Öffnen Sie ein Issue im Repository

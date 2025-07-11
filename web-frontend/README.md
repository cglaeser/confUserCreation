# Web Frontend for Conference User Management

A multilingual Flask web application providing an intuitive interface for managing conference users in Azure AD. This web frontend serves as a user-friendly wrapper around the PowerShell automation scripts.

## 🌐 Multilingual Support

The web interface supports **4 languages** with complete translations:
- **🇬🇧 English (en)** - Default language
- **🇩🇪 German (de)** - Deutsch  
- **🇪🇸 Spanish (es)** - Español
- **🇫🇮 Finnish (fi)** - Suomi

## 📁 Folder Structure

```
web-frontend/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── babel.cfg                       # Babel configuration for i18n
├── manage_translations.py          # Translation management utility
├── messages.pot                    # Translation template
├── 📁 templates/                   # Jinja2 HTML templates
│   ├── base.html                   # Base template with navigation
│   ├── index.html                  # Home page
│   ├── create.html                 # User creation form
│   ├── remove.html                 # User removal form
│   └── status.html                 # System status page
└── 📁 translations/                # Internationalization files
    ├── 📁 de/LC_MESSAGES/          # German translations
    │   ├── messages.po             # German source
    │   └── messages.mo             # German compiled
    ├── 📁 es/LC_MESSAGES/          # Spanish translations
    │   ├── messages.po             # Spanish source
    │   └── messages.mo             # Spanish compiled
    └── 📁 fi/LC_MESSAGES/          # Finnish translations
        ├── messages.po             # Finnish source
        └── messages.mo             # Finnish compiled
```

## 🚀 Quick Start

### Starting the Web Frontend
```bash
# From project root directory
./run.sh

# Or from this folder
python app.py

# Then open: http://localhost:5000
```

### Using the Interface
1. **🏠 Home Page**: Overview and navigation to all features
2. **➕ Create Users**: Form-based user creation with validation
3. **➖ Remove Users**: Safe user removal with preview options  
4. **📊 Status**: System diagnostics and requirements checking
5. **🌐 Language Switcher**: Click flags in navigation to change language

## ⚙️ Configuration

### Flask Settings
The application can be configured via environment variables:

```bash
export FLASK_ENV=development    # Development mode
export FLASK_DEBUG=1           # Enable debug mode
export FLASK_HOST=0.0.0.0      # Host address (default: 127.0.0.1)
export FLASK_PORT=5000         # Port number (default: 5000)
```

### Security Configuration
For production deployment, update the secret key in `app.py`:

```python
app.secret_key = 'your-secure-random-secret-key-here'
```

## 🔧 Development

### Setting Up Development Environment
```bash
# Install Python dependencies
pip install -r requirements.txt

# Start development server
python app.py
```

### Working with Translations

#### Managing Existing Languages
```bash
# Extract new translatable strings
python manage_translations.py extract

# Update existing translations with new strings
python manage_translations.py update

# Compile translations for use
python manage_translations.py compile

# Run full translation workflow
python manage_translations.py full
```

#### Adding New Languages
```bash
# Initialize new language (example: French)
python manage_translations.py init fr

# Edit the new translation file
# translations/fr/LC_MESSAGES/messages.po

# Add language to app.py configuration
# app.config['LANGUAGES']['fr'] = 'Français'

# Compile translations
python manage_translations.py compile
```

### Code Structure

#### Main Application (`app.py`)
- **Flask Configuration**: Basic app setup and internationalization
- **Route Handlers**: All web endpoints (`/`, `/create`, `/remove`, `/status`)
- **PowerShell Integration**: Subprocess calls to `../powershell-scripts/`
- **Form Validation**: Server-side validation for all user inputs
- **Error Handling**: Comprehensive error catching and user feedback

#### Templates (`templates/`)
- **base.html**: Common layout, navigation, and language switcher
- **index.html**: Landing page with feature overview
- **create.html**: User creation form with all PowerShell parameters
- **remove.html**: User removal form with safety confirmations  
- **status.html**: System diagnostics and requirements checking

#### Internationalization (`translations/`)
- **Babel Configuration**: Extraction and compilation settings
- **Translation Files**: Complete UI translations for all supported languages
- **Management Tools**: Utilities for maintaining translations

## 🎯 Features

### User Creation Interface
- **Conference Settings**: Name, user count, domain configuration
- **User Options**: Password policies, force password change
- **Azure Resources**: Optional resource group creation
- **Export Options**: Excel file output configuration
- **Execution Modes**: Dry-run preview and actual execution

### User Removal Interface  
- **Safe Removal**: Pattern-based user identification
- **Resource Cleanup**: Optional group and resource group removal
- **Security Features**: Confirmation dialogs and dry-run mode
- **Preview Mode**: Shows what will be removed before execution

### System Status Page
- **PowerShell Availability**: Checks for pwsh installation
- **Script Validation**: Verifies PowerShell scripts are accessible
- **Module Requirements**: Lists required PowerShell modules
- **Permissions**: Azure AD permission requirements
- **System Information**: Python, Flask, and environment details

### Multilingual Features
- **Language Auto-Detection**: Uses browser language preferences
- **Session Persistence**: Remembers selected language
- **Complete Translation**: All UI elements, forms, and messages
- **Professional Terminology**: Technical terms properly translated

## 🔌 PowerShell Integration

### Script Execution
The web frontend executes PowerShell scripts located in `../powershell-scripts/`:

```python
# User creation
ps_command = ['pwsh', '-File', '../powershell-scripts/New-ConferenceUsers.ps1']

# User removal  
ps_command = ['pwsh', '-File', '../powershell-scripts/Remove-ConferenceUsers.ps1']
```

### Parameter Passing
All form inputs are validated and passed as PowerShell parameters:

- **Conference Name**: `-ConferenceName "TechConf2024"`
- **User Count**: `-UserCount 10`
- **Domain**: `-Domain "contoso.onmicrosoft.com"`
- **Resource Groups**: `-CreateResourceGroups`
- **Dry Run**: `-DryRun`

### Output Handling
- **Real-time Progress**: Streams PowerShell output to web interface
- **Error Parsing**: Captures and displays PowerShell errors
- **Success Feedback**: Shows completion status and summary
- **Timeout Management**: Handles long-running operations

## 🛡️ Security Considerations

### Input Validation
- **Server-side Validation**: All form inputs validated before processing
- **Parameter Sanitization**: PowerShell injection prevention
- **File Path Security**: Restricted to allowed directories
- **Conference Name Patterns**: Alphanumeric with limited special characters

### Authentication & Authorization
- **No Built-in Auth**: Relies on network-level security
- **Azure AD Integration**: Uses underlying PowerShell authentication
- **Session Management**: Secure session handling for language preferences
- **Error Information**: Limited error details in production mode

### Production Security
- **HTTPS Required**: Use reverse proxy with SSL/TLS
- **Network Restrictions**: Limit access to trusted networks
- **Secret Key**: Use cryptographically secure secret key
- **Logging**: Monitor access and operations

## 🐛 Troubleshooting

### Common Issues

#### Flask Server Won't Start
```bash
# Check Python installation
python --version

# Install dependencies
pip install -r requirements.txt

# Check port availability
netstat -an | grep :5000
```

#### PowerShell Scripts Not Found
```bash
# Verify script locations
ls -la ../powershell-scripts/

# Check working directory
pwd
# Should be in web-frontend/ folder
```

#### Translation Issues
```bash
# Recompile translations
python manage_translations.py compile

# Check translation files
ls -la translations/*/LC_MESSAGES/
```

#### Permission Errors
```bash
# Check file permissions
chmod +x ../powershell-scripts/*.ps1

# Verify PowerShell installation
pwsh --version
```

### Error Messages

#### "PowerShell (pwsh) is not installed"
**Solution**: Install PowerShell Core
```bash
# Ubuntu/Debian
sudo apt install powershell

# Or download from Microsoft
# https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux
```

#### "Conference Name is required"
**Solution**: Form validation error - ensure all required fields are filled

#### "Timeout while executing PowerShell script"  
**Solution**: Operation took too long - try with fewer users or check Azure connectivity

## 📊 Monitoring & Logging

### Application Logs
The Flask application logs to console by default:
```python
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

### PowerShell Output
All PowerShell script output is captured and displayed in the web interface for real-time feedback.

### Production Logging
For production deployment, configure proper log handlers:
```python
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=10)
app.logger.addHandler(handler)
```

## 🚀 Deployment

### Development Deployment
```bash
# Quick start for development
python app.py
```

### Production Deployment
```bash
# Use a production WSGI server
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Or use uWSGI
pip install uwsgi
uwsgi --http :5000 --wsgi-file app.py --callable app
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 📄 Related Documentation

- **[Main Project README](../README.md)** - Overall project documentation
- **[PowerShell Scripts README](../powershell-scripts/README.md)** - Script documentation  
- **[Multilingual Setup Guide](../MULTILINGUAL_SETUP.md)** - Translation management
- **[Deployment Guide](../DEPLOYMENT.md)** - Production deployment

---

**Quick Start**: Run `python app.py` and open http://localhost:5000 in your browser!

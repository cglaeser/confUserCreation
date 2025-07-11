# Deployment Guide - Conference User Management Web Frontend

## Produktions-Deployment

### 1. Sicherheits-Konfiguration

**app.py bearbeiten:**
```python
# Sicheren Secret Key setzen
app.secret_key = 'your-very-secure-random-secret-key-here'

# Debug-Modus deaktivieren
app.run(debug=False, host='0.0.0.0', port=5000)
```

### 2. WSGI-Server (empfohlen)

**Gunicorn installieren:**
```bash
pip install gunicorn
```

**Starten mit Gunicorn:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Systemd Service erstellen:**
```bash
sudo nano /etc/systemd/system/conference-users.service
```

```ini
[Unit]
Description=Conference User Management Web Frontend
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/opt/confUserCreation
Environment="PATH=/opt/confUserCreation/venv/bin"
ExecStart=/opt/confUserCreation/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

**Service aktivieren:**
```bash
sudo systemctl enable conference-users
sudo systemctl start conference-users
```

### 3. Reverse Proxy (Nginx)

**Nginx-Konfiguration:**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 4. SSL/HTTPS (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

### 5. Umgebungsvariablen

**Environment File erstellen:**
```bash
# /opt/confUserCreation/.env
FLASK_SECRET_KEY=your-very-secure-secret-key
FLASK_ENV=production
FLASK_DEBUG=0
```

**App.py anpassen:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

app.secret_key = os.getenv('FLASK_SECRET_KEY', 'fallback-key')
```

## Docker Deployment

**Dockerfile erstellen:**
```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# PowerShell installieren
RUN curl -L -o /tmp/powershell.tar.gz https://github.com/PowerShell/PowerShell/releases/download/v7.3.6/powershell-7.3.6-linux-x64.tar.gz \
    && mkdir -p /opt/microsoft/powershell/7 \
    && tar zxf /tmp/powershell.tar.gz -C /opt/microsoft/powershell/7 \
    && chmod +x /opt/microsoft/powershell/7/pwsh \
    && ln -s /opt/microsoft/powershell/7/pwsh /usr/bin/pwsh

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

**Docker Compose:**
```yaml
version: '3.8'
services:
  conference-users:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_SECRET_KEY=your-secure-key
      - FLASK_ENV=production
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
```

## Monitoring und Logging

### 1. Logging-Konfiguration

**In app.py hinzufügen:**
```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
```

### 2. Health Check Endpoint

**In app.py hinzufügen:**
```python
@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'powershell_available': check_powershell(),
        'scripts_available': check_scripts()
    })
```

## Backup und Wartung

### 1. Automatisches Backup

**Backup-Skript:**
```bash
#!/bin/bash
# backup.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/conference-users"
SOURCE_DIR="/opt/confUserCreation"

mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/backup_$DATE.tar.gz -C $SOURCE_DIR .

# Alte Backups löschen (älter als 30 Tage)
find $BACKUP_DIR -name "backup_*.tar.gz" -mtime +30 -delete
```

**Crontab eintragen:**
```bash
0 2 * * * /opt/scripts/backup.sh
```

### 2. Log Rotation

**Logrotate-Konfiguration:**
```
/opt/confUserCreation/logs/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    copytruncate
}
```

## Sicherheits-Checkliste

- [ ] Secret Key geändert
- [ ] Debug-Modus deaktiviert
- [ ] HTTPS konfiguriert
- [ ] Firewall-Regeln gesetzt
- [ ] Reverse Proxy konfiguriert
- [ ] Logging aktiviert
- [ ] Backup-Strategie implementiert
- [ ] Monitoring eingerichtet
- [ ] Benutzer-Authentifizierung (falls erforderlich)
- [ ] Rate Limiting (optional)

## Performance-Optimierung

### 1. Caching

**Flask-Caching hinzufügen:**
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/status')
@cache.cached(timeout=60)
def status():
    # Cached für 60 Sekunden
    pass
```

### 2. Static Files

**Nginx für statische Dateien:**
```nginx
location /static {
    alias /opt/confUserCreation/static;
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

## Troubleshooting

### Häufige Probleme

1. **Port bereits belegt:**
   ```bash
   sudo netstat -tlnp | grep :5000
   sudo kill -9 <PID>
   ```

2. **PowerShell Berechtigungen:**
   ```bash
   sudo chmod +x /usr/bin/pwsh
   ```

3. **Disk Space:**
   ```bash
   df -h
   sudo find /var/log -name "*.log" -mtime +7 -delete
   ```

4. **Memory Issues:**
   ```bash
   free -h
   sudo systemctl restart conference-users
   ```

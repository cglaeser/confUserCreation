#!/usr/bin/env python3
"""
Flask Web Frontend for Conference User Management
Provides a web interface for creating and removing conference users
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_babel import Babel, gettext, ngettext, lazy_gettext
import subprocess
import json
import os
import logging
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Configure Babel for internationalization
app.config['LANGUAGES'] = {
    'en': 'English',
    'de': 'Deutsch',
    'es': 'Español',
    'fi': 'Suomi'
}
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel()

def get_current_locale():
    # 1. Check if language is set in session
    if 'language' in session:
        return session['language']
    # 2. Check if language is requested via URL parameter
    if request.args.get('lang'):
        session['language'] = request.args.get('lang')
        return session['language']
    # 3. Try to guess the language from the user accept header
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys()) or 'en'

# Initialize Babel with the app
babel.init_app(app, locale_selector=get_current_locale)

@app.route('/set_language/<language>')
def set_language(language=None):
    if language and language in app.config['LANGUAGES']:
        session['language'] = language
    return redirect(request.referrer or url_for('index'))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Template context processor to make gettext available in templates
@app.context_processor
def inject_conf_vars():
    return {
        'LANGUAGES': app.config['LANGUAGES'],
        'CURRENT_LANGUAGE': session.get('language', get_current_locale()),
        'AZURE_LOCATIONS': get_azure_locations(),
        'gettext': gettext,
        'ngettext': ngettext
    }

@app.route('/')
def index():
    """Main page with navigation options"""
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create_users():
    """Page for creating conference users"""
    if request.method == 'POST':
        # Get form data
        conference_name = request.form.get('conference_name', '').strip()
        user_count = request.form.get('user_count', '10')
        domain = request.form.get('domain', '').strip()
        password = request.form.get('password', '').strip()
        force_password_change = request.form.get('force_password_change') == 'on'
        create_resource_groups = request.form.get('create_resource_groups') == 'on'
        subscription_id = request.form.get('subscription_id', '').strip()
        location = request.form.get('location', '').strip()
        dry_run = request.form.get('dry_run') == 'on'
        excel_output_path = request.form.get('excel_output_path', '').strip()
        
        # Validate required fields
        if not conference_name:
            flash(gettext('Conference Name is required'), 'error')
            return render_template('create.html')
        
        if not location:
            flash(gettext('Location is required'), 'error')
            return render_template('create.html')
        
        try:
            user_count_int = int(user_count)
            if user_count_int < 1 or user_count_int > 1000:
                flash(gettext('User count must be between 1 and 1000'), 'error')
                return render_template('create.html')
        except ValueError:
            flash(gettext('User count must be a valid number'), 'error')
            return render_template('create.html')
        
        # Build PowerShell command
        project_root = os.path.dirname(os.getcwd())
        script_path = os.path.join(project_root, 'powershell-scripts', 'New-ConferenceUsers.ps1')
        ps_command = ['/usr/local/bin/pwsh', '-File', script_path]
        ps_command.extend(['-ConferenceName', conference_name])
        ps_command.extend(['-UserCount', str(user_count_int)])
        
        if domain:
            ps_command.extend(['-Domain', domain])
        if password:
            ps_command.extend(['-Password', password])
        
        ps_command.extend([f'-ForcePasswordChange:{str(force_password_change).lower()}'])
        ps_command.extend([f'-CreateResourceGroups:{str(create_resource_groups).lower()}'])
        
        if subscription_id:
            ps_command.extend(['-SubscriptionId', subscription_id])
        ps_command.extend(['-Location', location])
        if excel_output_path:
            ps_command.extend(['-ExcelOutputPath', excel_output_path])
        if dry_run:
            ps_command.append('-DryRun')
        
        # Execute PowerShell script
        try:
            logger.info(f"Executing command: {' '.join(ps_command)}")
            result = subprocess.run(
                ps_command,
                capture_output=True,
                text=True,
                cwd=project_root,
                timeout=300  # 5 minutes timeout
            )
            
            if result.returncode == 0:
                flash(gettext('Users created successfully! Conference: %(conference)s, Count: %(count)s', 
                             conference=conference_name, count=user_count), 'success')
                # Log the output for debugging
                logger.info(f"PowerShell output: {result.stdout}")
                if result.stderr:
                    logger.warning(f"PowerShell stderr: {result.stderr}")
            else:
                flash(gettext('Error creating users: %(error)s', error=result.stderr), 'error')
                logger.error(f"PowerShell error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            flash(gettext('Timeout while executing PowerShell script'), 'error')
        except FileNotFoundError:
            flash(gettext('PowerShell (pwsh) is not installed or not available in PATH'), 'error')
        except Exception as e:
            flash(gettext('Unexpected error: %(error)s', error=str(e)), 'error')
            logger.error(f"Unexpected error: {str(e)}")
        
        return redirect(url_for('create_users'))
    
    return render_template('create.html')

@app.route('/remove', methods=['GET', 'POST'])
def remove_users():
    """Page for removing conference users"""
    if request.method == 'POST':
        # Get form data
        conference_name = request.form.get('conference_name', '').strip()
        domain = request.form.get('domain', '').strip()
        remove_groups = request.form.get('remove_groups') == 'on'
        remove_resource_groups = request.form.get('remove_resource_groups') == 'on'
        force = request.form.get('force') == 'on'
        dry_run = request.form.get('dry_run') == 'on'
        
        # Validate required fields
        if not conference_name:
            flash(gettext('Conference Name is required'), 'error')
            return render_template('remove.html')
        
        # Build PowerShell command
        project_root = os.path.dirname(os.getcwd())
        script_path = os.path.join(project_root, 'powershell-scripts', 'Remove-ConferenceUsers.ps1')
        ps_command = ['/usr/local/bin/pwsh', '-File', script_path]
        ps_command.extend(['-ConferenceName', conference_name])
        
        if domain:
            ps_command.extend(['-Domain', domain])
        
        ps_command.extend([f'-RemoveGroups:{str(remove_groups).lower()}'])
        ps_command.extend([f'-RemoveResourceGroups:{str(remove_resource_groups).lower()}'])
        
        if force:
            ps_command.append('-Force')
        if dry_run:
            ps_command.append('-DryRun')
        
        # Execute PowerShell script
        try:
            logger.info(f"Executing command: {' '.join(ps_command)}")
            result = subprocess.run(
                ps_command,
                capture_output=True,
                text=True,
                cwd=project_root,
                timeout=300  # 5 minutes timeout
            )
            
            if result.returncode == 0:
                flash(gettext('Users removed successfully! Conference: %(conference)s', 
                             conference=conference_name), 'success')
                logger.info(f"PowerShell output: {result.stdout}")
                if result.stderr:
                    logger.warning(f"PowerShell stderr: {result.stderr}")
            else:
                flash(gettext('Error removing users: %(error)s', error=result.stderr), 'error')
                logger.error(f"PowerShell error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            flash(gettext('Timeout while executing PowerShell script'), 'error')
        except FileNotFoundError:
            flash(gettext('PowerShell (pwsh) is not installed or not available in PATH'), 'error')
        except Exception as e:
            flash(gettext('Unexpected error: %(error)s', error=str(e)), 'error')
            logger.error(f"Unexpected error: {str(e)}")
        
        return redirect(url_for('remove_users'))
    
    return render_template('remove.html')

@app.route('/status')
def status():
    """Status page showing system information"""
    status_info = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'powershell_available': check_powershell(),
        'scripts_available': check_scripts()
    }
    return render_template('status.html', status=status_info)

def check_powershell():
    """Check if PowerShell is available"""
    try:
        result = subprocess.run(['/usr/local/bin/pwsh', '--version'], capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except:
        return False

def check_scripts():
    """Check if PowerShell scripts are available"""
    scripts = ['powershell-scripts/New-ConferenceUsers.ps1', 'powershell-scripts/Remove-ConferenceUsers.ps1']
    available = {}
    project_root = os.path.dirname(os.getcwd())
    for script in scripts:
        script_path = os.path.join(project_root, script)
        available[f'../{script}'] = os.path.exists(script_path)
    return available

def get_azure_locations():
    """Get list of Azure locations for dropdown"""
    return [
        ('eastus', 'East US'),
        ('eastus2', 'East US 2'),
        ('centralus', 'Central US'),
        ('northcentralus', 'North Central US'),
        ('southcentralus', 'South Central US'),
        ('westcentralus', 'West Central US'),
        ('westus', 'West US'),
        ('westus2', 'West US 2'),
        ('westus3', 'West US 3'),
        ('canadacentral', 'Canada Central'),
        ('canadaeast', 'Canada East'),
        ('brazilsouth', 'Brazil South'),
        ('northeurope', 'North Europe'),
        ('westeurope', 'West Europe'),
        ('francecentral', 'France Central'),
        ('francesouth', 'France South'),
        ('germanynorth', 'Germany North'),
        ('germanywestcentral', 'Germany West Central'),
        ('norwayeast', 'Norway East'),
        ('norwaywest', 'Norway West'),
        ('switzerlandnorth', 'Switzerland North'),
        ('switzerlandwest', 'Switzerland West'),
        ('uksouth', 'UK South'),
        ('ukwest', 'UK West'),
        ('swedencentral', 'Sweden Central'),
        ('swedensouth', 'Sweden South'),
        ('eastasia', 'East Asia'),
        ('southeastasia', 'Southeast Asia'),
        ('australiacentral', 'Australia Central'),
        ('australiacentral2', 'Australia Central 2'),
        ('australiaeast', 'Australia East'),
        ('australiasoutheast', 'Australia Southeast'),
        ('centralindia', 'Central India'),
        ('southindia', 'South India'),
        ('westindia', 'West India'),
        ('japaneast', 'Japan East'),
        ('japanwest', 'Japan West'),
        ('koreacentral', 'Korea Central'),
        ('koreasouth', 'Korea South'),
        ('southafricanorth', 'South Africa North'),
        ('southafricawest', 'South Africa West'),
        ('uaenorth', 'UAE North'),
        ('uaecentral', 'UAE Central'),
        ('qatarcentral', 'Qatar Central'),
    ]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

#!/usr/bin/env python3
"""
Translation Management Utility for Conference User Management
Helps extract, update, and compile translations
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ Success: {description}")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {description}")
        print(f"Error: {e.stderr}")
        return False

def extract_messages():
    """Extract translatable strings from the application"""
    cmd = "pybabel extract -F babel.cfg -k _l -o messages.pot ."
    return run_command(cmd, "Extracting messages from source files")

def update_translations():
    """Update existing translation files with new strings"""
    cmd = "pybabel update -i messages.pot -d translations"
    return run_command(cmd, "Updating translation files")

def compile_translations():
    """Compile .po files to .mo files"""
    cmd = "pybabel compile -d translations"
    return run_command(cmd, "Compiling translation files")

def init_language(lang_code):
    """Initialize a new language"""
    cmd = f"pybabel init -i messages.pot -d translations -l {lang_code}"
    return run_command(cmd, f"Initializing {lang_code} language")

def show_help():
    """Show help information"""
    print("""
Conference User Management - Translation Management

Usage: python manage_translations.py [command]

Commands:
  extract     Extract translatable strings from source files
  update      Update existing translations with new strings
  compile     Compile translation files (.po to .mo)
  full        Run extract, update, and compile in sequence
  init <lang> Initialize a new language (e.g., 'fr' for French)
  help        Show this help message

Examples:
  python manage_translations.py extract
  python manage_translations.py full
  python manage_translations.py init fr
    """)

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "extract":
        extract_messages()
    elif command == "update":
        update_translations()
    elif command == "compile":
        compile_translations()
    elif command == "full":
        print("Running full translation update process...")
        if extract_messages():
            if update_translations():
                compile_translations()
    elif command == "init":
        if len(sys.argv) < 3:
            print("Error: Please specify language code (e.g., 'fr' for French)")
            return
        lang_code = sys.argv[2]
        # First extract messages if messages.pot doesn't exist
        if not os.path.exists("messages.pot"):
            extract_messages()
        init_language(lang_code)
    elif command == "help":
        show_help()
    else:
        print(f"Unknown command: {command}")
        show_help()

if __name__ == "__main__":
    main()

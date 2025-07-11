# Conference User Management - Multilingual Setup

## Overview
The Conference User Management web frontend now supports multiple languages with full internationalization (i18n) using Flask-Babel.

## Supported Languages
- **English (en)** - Default language
- **German (de)** - Deutsch
- **Spanish (es)** - Español
- **Finnish (fi)** - Suomi

## Features
- Language switcher in the navigation bar with flag icons
- Automatic language detection from browser settings
- Session-based language persistence
- Complete translation of UI elements, forms, and messages

## Quick Start

### Starting the Multilingual Frontend
```bash
# Option 1: Using the start script
./start-frontend.sh

# Option 2: Direct Python execution
python app.py

# Option 3: Using the run script
./run.sh
```

The web interface will be available at: http://localhost:5000

### Switching Languages
1. Click on the language switcher in the navigation bar
2. Select your preferred language from the dropdown
3. The interface will immediately switch to the selected language
4. Your language preference is saved in the browser session

## Translation Management

### Managing Translations
Use the included translation management script:

```bash
# Extract new translatable strings
python manage_translations.py extract

# Update existing translations with new strings
python manage_translations.py update

# Compile translations for use
python manage_translations.py compile

# Run full translation update process
python manage_translations.py full

# Initialize a new language (e.g., French)
python manage_translations.py init fr
```

### Manual Translation Process
1. **Extract strings**: `pybabel extract -F babel.cfg -k _l -o messages.pot .`
2. **Update translations**: `pybabel update -i messages.pot -d translations`
3. **Edit .po files**: Update translations in `translations/[lang]/LC_MESSAGES/messages.po`
4. **Compile**: `pybabel compile -d translations`

### Adding New Languages
1. Extract messages: `python manage_translations.py extract`
2. Initialize new language: `python manage_translations.py init [lang_code]`
3. Edit the new .po file in `translations/[lang_code]/LC_MESSAGES/messages.po`
4. Add the language to `app.py` in the `LANGUAGES` configuration:
   ```python
   app.config['LANGUAGES'] = {
       'en': 'English',
       'de': 'Deutsch',
       'es': 'Español',
       'fi': 'Suomi',
       'fr': 'Français'  # New language
   }
   ```
5. Compile translations: `python manage_translations.py compile`

## Technical Implementation

### Flask-Babel Configuration
- **Locale Selector**: Automatic language detection based on:
  1. Session language preference
  2. URL parameter (`?lang=de`)
  3. Browser Accept-Language header
  4. Default to English

### File Structure
```
/workspaces/confUserCreation/
├── app.py                          # Main Flask application
├── babel.cfg                       # Babel configuration
├── manage_translations.py          # Translation management utility
├── translations/                   # Translation files
│   ├── de/LC_MESSAGES/
│   │   ├── messages.po            # German translations (source)
│   │   └── messages.mo            # German translations (compiled)
│   ├── es/LC_MESSAGES/
│   │   ├── messages.po            # Spanish translations (source)
│   │   └── messages.mo            # Spanish translations (compiled)
│   └── fi/LC_MESSAGES/
│       ├── messages.po            # Finnish translations (source)
│       └── messages.mo            # Finnish translations (compiled)
└── templates/                      # HTML templates with gettext() calls
    ├── base.html                  # Base template with language switcher
    ├── index.html                 # Home page
    ├── create.html                # User creation form
    ├── remove.html                # User removal form
    └── status.html                # System status page
```

### Translation Keys
All user-facing text uses `gettext()` function calls:
```html
<!-- In templates -->
{{ gettext('Conference User Management') }}
{{ gettext('Create Users') }}

<!-- In Python code -->
flash(gettext('Users created successfully!'))
```

## Language-Specific Features

### Finnish (Suomi)
- Complete translation of all UI elements
- Standard Finnish terminology for technical terms
- Professional business Finnish language

### German (Deutsch)
- Complete translation of all UI elements
- Proper German terminology for technical terms
- Formal addressing style ("Sie" form)

### Spanish (Español)
- Complete translation of all UI elements
- Standard international Spanish
- Professional terminology

### English
- Default language
- Source language for all translations
- Professional technical English

## Browser Compatibility
- Language switcher works in all modern browsers
- Responsive design maintains language selector on mobile devices
- Flag icons display correctly across platforms

## Troubleshooting

### Common Issues
1. **Language not switching**: Check if translations are compiled (`python manage_translations.py compile`)
2. **Missing translations**: Run `python manage_translations.py update` and edit .po files
3. **Server errors**: Ensure Flask-Babel is properly installed and configured

### Development Tips
- Always run `pybabel compile -d translations` after editing .po files
- Use `gettext()` for all new user-facing strings
- Test language switching in different browsers
- Keep translations consistent in terminology

## Future Enhancements
- Additional language support (French, Italian, Portuguese)
- Right-to-left language support (Arabic, Hebrew)
- Date/time localization
- Number format localization
- Currency format localization

## Dependencies
- Flask
- Flask-Babel
- Babel
- Bootstrap 5 (for UI framework)
- Font Awesome (for flag icons)

---

For technical support or translation contributions, please refer to the main project documentation.

#!/bin/bash

# Translation Management Script for Conference User Management
# This script helps with extracting, updating and compiling translations

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================${NC}"
echo -e "${BLUE}  Translation Management Tool        ${NC}"
echo -e "${BLUE}  Conference User Management          ${NC}"
echo -e "${BLUE}======================================${NC}"
echo

# Check if pybabel is available
if ! command -v pybabel &> /dev/null; then
    echo -e "${RED}Error: pybabel is not installed!${NC}"
    echo -e "${YELLOW}Please install Flask-Babel: pip install Flask-Babel${NC}"
    exit 1
fi

# Function to extract translatable strings
extract_messages() {
    echo -e "${YELLOW}Extracting translatable strings...${NC}"
    pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
    echo -e "${GREEN}✓ Strings extracted to messages.pot${NC}"
}

# Function to update existing translations
update_translations() {
    echo -e "${YELLOW}Updating existing translations...${NC}"
    
    for lang in de es; do
        if [ -f "translations/$lang/LC_MESSAGES/messages.po" ]; then
            echo -e "${BLUE}Updating $lang translation...${NC}"
            pybabel update -i messages.pot -d translations -l $lang
            echo -e "${GREEN}✓ Updated $lang${NC}"
        else
            echo -e "${YELLOW}Creating new $lang translation...${NC}"
            pybabel init -i messages.pot -d translations -l $lang
            echo -e "${GREEN}✓ Created $lang${NC}"
        fi
    done
}

# Function to compile translations
compile_translations() {
    echo -e "${YELLOW}Compiling translations...${NC}"
    pybabel compile -d translations
    echo -e "${GREEN}✓ Translations compiled${NC}"
}

# Function to add a new language
add_language() {
    local lang=$1
    if [ -z "$lang" ]; then
        echo -e "${RED}Error: Language code required${NC}"
        echo -e "${YELLOW}Usage: $0 add <language_code>${NC}"
        echo -e "${YELLOW}Example: $0 add fr${NC}"
        exit 1
    fi
    
    echo -e "${YELLOW}Adding new language: $lang${NC}"
    
    if [ ! -f "messages.pot" ]; then
        echo -e "${YELLOW}Extracting messages first...${NC}"
        extract_messages
    fi
    
    pybabel init -i messages.pot -d translations -l $lang
    echo -e "${GREEN}✓ Language $lang added${NC}"
    echo -e "${YELLOW}Please edit translations/$lang/LC_MESSAGES/messages.po to add translations${NC}"
}

# Function to show statistics
show_stats() {
    echo -e "${YELLOW}Translation Statistics:${NC}"
    echo
    
    for lang_dir in translations/*/; do
        if [ -d "$lang_dir" ]; then
            lang=$(basename "$lang_dir")
            po_file="$lang_dir/LC_MESSAGES/messages.po"
            
            if [ -f "$po_file" ]; then
                total=$(grep -c "^msgid " "$po_file" || echo "0")
                translated=$(grep -c "^msgstr \"[^\"]\+\"" "$po_file" || echo "0")
                empty=$(grep -c "^msgstr \"\"" "$po_file" || echo "0")
                
                percentage=0
                if [ "$total" -gt 0 ]; then
                    percentage=$((translated * 100 / total))
                fi
                
                echo -e "${BLUE}$lang:${NC} $translated/$total translated (${percentage}%), $empty empty"
            fi
        fi
    done
    echo
}

# Function to show help
show_help() {
    echo -e "${BLUE}Translation Management Tool${NC}"
    echo
    echo -e "${YELLOW}Usage:${NC}"
    echo "  $0 extract                 - Extract translatable strings"
    echo "  $0 update                  - Update existing translations"
    echo "  $0 compile                 - Compile translations to binary"
    echo "  $0 add <lang>              - Add a new language"
    echo "  $0 stats                   - Show translation statistics"
    echo "  $0 full                    - Extract, update and compile (full workflow)"
    echo "  $0 help                    - Show this help"
    echo
    echo -e "${YELLOW}Examples:${NC}"
    echo "  $0 full                    - Complete translation workflow"
    echo "  $0 add fr                  - Add French translation"
    echo "  $0 stats                   - Show completion status"
    echo
    echo -e "${YELLOW}Supported Languages:${NC}"
    echo "  de - German (Deutsch)"
    echo "  es - Spanish (Español)"
    echo "  en - English (default)"
    echo
}

# Main script logic
case "${1:-help}" in
    extract)
        extract_messages
        ;;
    update)
        update_translations
        ;;
    compile)
        compile_translations
        ;;
    add)
        add_language "$2"
        ;;
    stats)
        show_stats
        ;;
    full)
        extract_messages
        echo
        update_translations
        echo
        compile_translations
        echo
        show_stats
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        echo
        show_help
        exit 1
        ;;
esac

echo -e "${GREEN}Done!${NC}"

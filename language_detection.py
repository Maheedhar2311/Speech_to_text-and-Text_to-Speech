from text_display import get_language_code
from error_handling import show_warning

def fetch_language_code() -> str:
    lang = get_language_code()
    if not lang:
        show_warning("Language Code Missing", "Please enter a language code (e.g., 'fr', 'es').")
    return lang

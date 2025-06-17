from googletrans import Translator  # type: ignore
from text_display import get_output_text, set_translated_text, set_status_text
from language_detection import fetch_language_code
from error_handling import show_error, show_warning

def translate_text() -> None:
    input_text = get_output_text()
    dest_lang = fetch_language_code()

    if not input_text:
        show_warning("Input Missing", "Please speak or enter text first.")
        return
    if not dest_lang:
        return

    try:
        translator = Translator()
        translated = translator.translate(input_text, dest=dest_lang)
        set_translated_text(translated.text)
        set_status_text(f"Translated to {dest_lang.upper()}.")
    except Exception as e:
        show_error("Translation Error", str(e))
        set_status_text("Translation failed.")

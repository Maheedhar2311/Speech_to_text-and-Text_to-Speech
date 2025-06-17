
import pyttsx3  # type: ignore
from text_display import get_translated_text, get_language_code
from error_handling import show_error
import platform

def speak_translatedtext() -> None:
    text = get_translated_text()
    if not text:
        show_error("No Text", "No translated text available to speak.")
        return

    try:
        engine = pyttsx3.init()
        
        # Set properties
        engine.setProperty('rate', 150)  # Moderate speaking speed
        engine.setProperty('volume', 1.0)  # Max volume
        
        # Language handling
        lang_code = get_language_code()
        if lang_code:
            voices = engine.getProperty('voices')
            lang_code = lang_code.lower()
            
            # Platform-specific voice selection
            if platform.system() == "Windows":
                for voice in voices:
                    if lang_code in voice.id.lower():
                        engine.setProperty('voice', voice.id)
                        break
            else:  # Mac/Linux
                for voice in voices:
                    if hasattr(voice, 'languages') and voice.languages:
                        if lang_code in str(voice.languages[0]).lower():
                            engine.setProperty('voice', voice.id)
                            break
        
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        show_error("Speech Error", f"Text-to-speech failed: {str(e)}")

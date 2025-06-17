import speech_recognition as sr  # type: ignore
from text_display import set_output_text, set_status_text
from error_handling import show_error

def recognize_speech() -> str:
    recognizer = sr.Recognizer() 

    try:
        mic_list = sr.Microphone.list_microphone_names()
        if not mic_list:
            show_error("Microphone Error", "No microphone detected.")
            return ""

        with sr.Microphone() as source:
            set_output_text("Listening...")
            set_status_text("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio)
        set_output_text(text)
        set_status_text("Speech recognized successfully.")
        return text

    except sr.WaitTimeoutError:
        show_error("Timeout", "Listening timed out while waiting for phrase.")
    except sr.UnknownValueError:
        show_error("Speech Error", "Could not understand audio.")
    except sr.RequestError:
        show_error("Connection Error", "Could not connect to Google Speech service.")
    except OSError:
        show_error("Microphone Error", "Microphone not accessible or not working.")

    set_status_text("Speech recognition failed.")
    return ""

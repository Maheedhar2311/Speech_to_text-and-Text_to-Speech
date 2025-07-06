🎙️ Speech to Text Translator:
- A cross_platform GUI application that converts speech to text and translates it into multiple languages and converts the translated text to speech.
- Built using python and tkinter

📦 Features:
- Speech Recognition using your system’s microphone
- Language Translation into any supported language (using ISO language codes)
- Translated language to speech only for supported languages
- User-friendly interface built with Tkinter
- Real-time error and warning messages via message boxes


🛠️ Dependencies:
Make sure the following Python packages are installed:
pip install SpeechRecognition
pip install googletrans==4.0.0-rc1
pip install pyttsx3 gtts playsound
pip install pyaudio  # For microphone access


🗂️ Project Structure:
.
├── main.py                       # GUI entry point
├── speech_recognition_module.py  # Handles speech input
├── text_translation.py           # Handles language translation
├── text_display.py               # Manages shared text variables
├── language_detection.py         # Validates language code input
├── error_handling.py             # Centralized error & warning popups
├── my_speech.py                  # Converts translated text to speech
└── README.md                     # Documentation file


🚀 How to Run
Ensure your microphone is connected and working.

1. Run the main GUI application:
    python3 main.py (OR) directly run it on VSCode
2. Click the 🎤 Speak button and say something.
3. Select a language from languages provided in a dropdown.
4. Click "Translate" button to see the translation.
5. Click "Speak Translated" button to see the pronounciation.

❗ Troubleshooting:
- Microphone not found: Ensure it is connected and selected as the default input device.
- Translation fails: Check internet connection or make sure the language code is valid.
- Speech not detected: Try speaking louder or adjusting for ambient noise.
- Text to Speech fails : For some languages that are not supportive.

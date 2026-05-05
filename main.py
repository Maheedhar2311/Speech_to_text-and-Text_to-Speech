# Import required modules
import tkinter as tk                         # GUI library for creating the app window
import text_display as display              # Custom module to manage shared variables/UI elements
from my_speech import recognize_speech      # Function to convert speech → text
from text_translation import translate_text # Function to translate text
from text_speech import speak_translatedtext # Function to convert translated text → speech


# -------------------- WINDOW SETUP --------------------

# Create main application window
window = tk.Tk()

# Set window title
window.title("🎙️ Speech to Text Translator")

# Set window size (width x height)
window.geometry("500x420")

# Set background color
window.config(bg="#f4f4f4")


# -------------------- INITIALIZE DISPLAY VARIABLES --------------------

# Initialize variables (like StringVar for text fields)
display.initialize_variables(window)


# -------------------- STATUS LABEL --------------------

# Create a label to show app status (e.g., Ready, Listening, Translating)
status_label = tk.Label(
    window,
    text="Ready",
    bg="#f4f4f4",
    fg="#333333"
)

# Add it to the window
status_label.pack(pady=5)

# Pass this label to display module so other functions can update it
display.set_status_label(status_label)


# -------------------- TITLE LABEL --------------------

# App heading
tk.Label(
    window,
    text="Speech to Text",
    font=("Helvetica", 16),
    bg="#f4f4f4",
    fg="#000000"
).pack(pady=10)


# -------------------- SPEECH BUTTON --------------------

# Button to start speech recognition
tk.Button(
    window,
    text="🎤 Speak",
    font=("Helvetica", 12),
    command=recognize_speech   # Calls speech recognition function
).pack(pady=5)


# -------------------- RECOGNIZED TEXT INPUT --------------------

# Label for recognized text
tk.Label(
    window,
    text="Recognized Text:",
    bg="#f4f4f4",
    fg="#000000"
).pack()

# Entry field to display recognized speech text
tk.Entry(
    window,
    textvariable=display.output_text,  # Linked to variable from display module
    width=60
).pack(pady=5)


# -------------------- LANGUAGE OPTIONS --------------------

# Dictionary mapping language names → language codes
language_options = {
    "Amharic":"am","Arabic":"ar","Basque":"eu","Bengali":"bn","Bulgarian":"bg",
    "Catalan":"ca","Croatian":"hr","Czech":"cs","Danish":"da","Dutch":"nl",
    "English(US)":"en","Estonian":"et","Finnish":"fi","French":"fr","German":"de",
    "Greek":"el","Gujarati":"gu","Hebrew":"iw","Hindi":"hi","Hungarian":"hu",
    "Icelandic":"is","Indonesian":"id","Italian":"it","Japanese":"ja","Kannada":"kn",
    "Korean":"ko","Latvian":"lv","Lithuanian":"lt","Malay":"ms","Malayalam":"ml",
    "Marathi":"mr","Norwegian":"no","Polish":"pl","Romanian":"ro","Russian":"ru",
    "Serbian":"sr","Chinese(PRC)":"zh-CN","Slovak":"sk","Slovenian":"sl",
    "Spanish":"es","Swahili":"sw","Swedish":"sv","Tamil":"ta","Telugu":"te",
    "Thai":"th","Chinese(Taiwan)":"zh-TW","Turkish":"tr","Urdu":"ur",
    "Ukranian":"uk","Vietnamese":"vi","Welsh":"cy"
}

# Variable to store selected language from dropdown
default_lang = tk.StringVar(window)

# Set default language shown in dropdown
default_lang.set("English(US)")

# Set default language code internally
display.language_code.set("en")  


# -------------------- LANGUAGE UPDATE FUNCTION --------------------

# Function to update language code when user selects a different language
def update_language(selection):
    display.language_code.set(language_options[selection])


# -------------------- LANGUAGE DROPDOWN --------------------

# Label for language selection
tk.Label(
    window,
    text="Translate To:",
    bg="#f4f4f4",
    fg="#000000"
).pack()

# Dropdown menu for selecting language
tk.OptionMenu(
    window,
    default_lang,
    *language_options.keys(),   # All language names
    command=update_language     # Update language code on selection
).pack(pady=5)


# -------------------- TRANSLATE BUTTON --------------------

# Button to translate recognized text
tk.Button(
    window,
    text="🌍 Translate",
    font=("Helvetica", 12),
    command=translate_text      # Calls translation function
).pack(pady=5)


# -------------------- TRANSLATED TEXT OUTPUT --------------------

# Label for translated text
tk.Label(
    window,
    text="Translated Text:",
    bg="#f4f4f4",
    fg="#000000"
).pack()

# Entry field to display translated text
tk.Entry(
    window,
    textvariable=display.translated_text,  # Linked to translated output variable
    width=60
).pack(pady=5)


# -------------------- TEXT-TO-SPEECH BUTTON --------------------

# Button to speak translated text
tk.Button(
    window,
    text="🔊 Speak Translation",
    font=("Helvetica", 12),
    command=speak_translatedtext  # Calls text-to-speech function
).pack(pady=5)


# -------------------- MAIN LOOP --------------------

# Run the GUI application
window.mainloop()

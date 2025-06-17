import tkinter as tk
import text_display as display
from my_speech import recognize_speech
from text_translation import translate_text
from text_speech import speak_translatedtext #type:ignore
window = tk.Tk()
window.title("🎙️ Speech to Text Translator")
window.geometry("500x420")
window.config(bg="#f4f4f4")

display.initialize_variables(window)
# Add this near the top of main.py (after initialize_variables)
status_label = tk.Label(window, text="Ready", bg="#f4f4f4", fg="#333333")
status_label.pack(pady=5)
display.set_status_label(status_label)

tk.Label(window, text="Speech to Text", font=("Helvetica", 16), bg="#f4f4f4",fg="#000000").pack(pady=10)
tk.Button(window, text="🎤 Speak", font=("Helvetica", 12), command=recognize_speech).pack(pady=5)

tk.Label(window, text="Recognized Text:", bg="#f4f4f4",fg="#000000").pack()
tk.Entry(window, textvariable=display.output_text, width=60).pack(pady=5)

language_options = {
    "Amharic":"am","Arabic":"ar","Basque":"eu","Bengali":"bn","Bulgarian":"bg",
    "Catalan":"ca","Croatian":"hr","Czech":"cs","Danish":"da","Dutch":"nl","English(US)":"en","Estonian":"et",
   "Finnish":"fi","French":"fr","German":"de","Greek":"el","Gujarati":"gu","Hebrew":"iw","Hindi":"hi","Hungarian":"hu",
    "Icelandic":"is","Indonesian":"id","Italian":"it","Japanese":"ja","Kannada":"kn","Korean":"ko","Latvian":"lv","Lithuanian":"lt",
    "Malay":"ms","Malayalam":"ml","Marathi":"mr","Norwegian":"no","Polish":"pl","Romanian":"ro","Russian":"ru",
    "Serbian":"sr","Chinese(PRC)":"zh-CN","Slovak":"sk","Slovenian":"sl","Spanish":"es","Swahili":"sw","Swedish":"sv","Tamil":"ta",
    "Telugu":"te","Thai":"th","Chinese(Taiwan)":"zh-TW","Turkish":"tr","Urdu":"ur","Ukranian":"uk","Vietnamese":"vi","Welsh":"cy"
}
default_lang = tk.StringVar(window)
default_lang.set("English(US)")
display.language_code.set("en")  
def update_language(selection):
    display.language_code.set(language_options[selection])

tk.Label(window, text="Translate To:", bg="#f4f4f4", fg="#000000").pack()
tk.OptionMenu(window, default_lang, *language_options.keys(), command=update_language).pack(pady=5)


tk.Button(window, text="🌍 Translate", font=("Helvetica", 12), command=translate_text).pack(pady=5)

tk.Label(window, text="Translated Text:", bg="#f4f4f4",fg="#000000").pack()
tk.Entry(window, textvariable=display.translated_text, width=60).pack(pady=5)
tk.Button(window, text="🔊 Speak Translation", font=("Helvetica", 12), command=speak_translatedtext).pack(pady=5)

window.mainloop()
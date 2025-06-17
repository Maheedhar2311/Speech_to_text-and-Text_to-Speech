import tkinter as tk

output_text = None
translated_text = None
language_code = None
status_label = None

def initialize_variables(master):
    global output_text, translated_text, language_code
    output_text = tk.StringVar(master)
    translated_text = tk.StringVar(master)
    language_code = tk.StringVar(master)

def set_output_text(text: str) -> None:
    output_text.set(text)

def get_output_text() -> str:
    return output_text.get()

def set_translated_text(text: str) -> None:
    translated_text.set(text)

def get_translated_text() -> str:
    return translated_text.get()

def set_language_code(text: str) -> None:
    language_code.set(text)

def get_language_code() -> str:
    return language_code.get()

def clear_all_fields() -> None:
    output_text.set("")
    translated_text.set("")
    language_code.set("")

def set_status_label(label_widget):
    global status_label
    status_label = label_widget

def set_status_text(text: str):
    if status_label:
        status_label.config(text=text)

from tkinter import messagebox

def show_error(title: str, message: str) -> None:
    messagebox.showerror(title, message)

def show_warning(title: str, message: str) -> None:
    messagebox.showwarning(title, message)
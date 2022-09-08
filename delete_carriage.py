import re
from tkinter import Tk

clipboard_text = Tk().clipboard_get()
clipboard_text = re.sub(r"\n([^А-Я|^A-Z])", r" \1", clipboard_text)
clipboard_text = re.sub(r"(\w)\n(\w)", r"\1\n\n\2", clipboard_text)
clipboard_text = re.sub(r"(\w)( -|- )(\w)", r"\1 - \3", clipboard_text)

with open("Texts/post_carriage.txt", "a") as file: 
    file.write(clipboard_text + "\n")

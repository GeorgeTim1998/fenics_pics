import re
from tkinter import Tk

clipboard_text = Tk().clipboard_get()
clipboard_text = re.sub(r"\n([^А-Я])", r" \1", clipboard_text)
clipboard_text = clipboard_text.replace("\n", "\n\n")

with open("Texts/post_carriage.txt", "a") as file: 
    file.write(clipboard_text + "\n\n")

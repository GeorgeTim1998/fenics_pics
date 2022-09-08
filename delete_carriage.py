import re
from tkinter import Tk

re_sub_args = {
    r"\n([^А-Я|^A-Z])": r" \1",
    r"(\w)\n([А-Я|A-Z])": r"\1 \2",
    r"(\w.)\n(\w)": r"\1\n\n\2",
    r"(\w)( -|- )(\w)": r"\1 - \3"
    }

clipboard_text = Tk().clipboard_get()

for pattern, repl in re_sub_args.items():
    clipboard_text = re.sub(pattern, repl, clipboard_text)

with open("Texts/post_carriage.txt", "a") as file: 
    file.write("\n" + clipboard_text + "\n")

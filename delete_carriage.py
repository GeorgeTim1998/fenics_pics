from tkinter import Tk

clipboard_text = Tk().clipboard_get().replace("\n", " ")

with open("Texts/post_carriage.txt", "a") as file: 
    file.write(clipboard_text + "\n\n")

from tkinter import Tk

clipboard_text = Tk().clipboard_get().replace("\n", " ")

file = open("Texts/post_carriage.txt", "w")
file.write(clipboard_text)
file.close()
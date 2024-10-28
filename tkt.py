import tkinter as tk

text='salaamo3alaykom'


def ma_fonction(event):
    text=str(event.char)
    label = tk.Label(root, text=text)
    label.pack()
    

root = tk.Tk()
root.geometry('920x700')
root.config(bg="grey")

# Création d'un label avec du texte
label = tk.Label(root, text=text)
label.pack()

root.bind("<Key>", ma_fonction) 


root.mainloop()

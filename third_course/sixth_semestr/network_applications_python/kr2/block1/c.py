from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
languages = ["Python", "C#", "Java", "JavaScript"]
combobox = ttk.Combobox(values=languages)
combobox.pack(anchor=NW, padx=6, pady=6)
 
root.mainloop()
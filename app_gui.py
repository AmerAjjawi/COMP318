#scaffolding for tkinter will be added here
from tkinter import *
from tkinter import ttk

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Sentiment Analysis").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
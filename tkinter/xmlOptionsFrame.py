import tkinter as tk

class XMLOptionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()

        self.loadXML = tk.Button(self, text="Load XML File", command=parent.loadXMLFile)
        self.loadXML.grid(row=0, column=0, padx=10)

        self.lenLabel = tk.Label(self, text="Min. Length to Process")
        self.lenLabel.grid(row=0, column=1, padx=5)

        self.lenScale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.lenScale.grid(row=0, column=2, padx=10)

        self.btnClearText = tk.Button(self, text="Clear Text", command=parent.clearText)
        self.btnClearText.grid(row=0, column=3, padx=10)
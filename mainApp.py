import tkinter as tk
from tkinter import filedialog

import xml.etree.ElementTree as ET

from xmlOptionsFrame import XMLOptionsFrame

class App(tk.Tk):
    #Top level of App
    def __init__(self):
        super().__init__()
        self.title("COMP318 Final - NTLK Canadian Act Analyizer")
        self.geometry("640x480+50+50")

        self.textfield = tk.Text(self, width=80, height=27)
        self.textfield.pack()

        self.xmlFrame = XMLOptionsFrame(self)
        self.actText = "" #holds text for analysis

    #Called when user opens XML file via filedialog. Parses XML data to get text of act
    def loadXMLFile(self):
        self.xmlFile = filedialog.askopenfilename(
                initialdir="", 
                title="Select XML",
                filetypes=(("XML files", "*.xml"), ("All Files", "*.*"))
            )
        
        if self.xmlFile:
            xmlDoc = ET.parse(self.xmlFile)

            for elem in xmlDoc.iter():
                if elem.text and (len(elem.text) >= self.xmlFrame.lenScale.get()):
                    self.textfield.insert(tk.END, elem.text + "\n")
                    self.actText += elem.text

        print(self.actText)

    #Clears the text field
    def clearText(self):
        self.textfield.delete(1.0, tk.END)

app = App()
app.mainloop()
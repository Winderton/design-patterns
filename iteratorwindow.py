from tkinter import *

from behavioral.iterator import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Search")
        self.geometry("640x480")
        self.samples = Samples(['hat', 'kick', '808'])

        self.entry = Entry(self)
        self.entry.pack()
        self.entry.bind('<KeyPress>', self.parse)

        self.listbox = Listbox(self)
        self.listbox.pack()

    def parse(self, e):
        self.listbox.delete(0, 'end')

        char = e.widget.get()
        data = []

        for item in self.samples:
            if char in item:
                data.append(item)
            if not char and not char.isspace():
                return
            
        self.listbox.delete(0, 'end')
        for item in data:
            self.listbox.insert(0, item)

        
from tkinter import Toplevel, Button
from creational.abstractfactory import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("EQs")
        self.geometry("640x480")
        
        self.button = Button(self, text='Show EQs', command=self.show_EQs)
        self.button.pack(expand=True)



    def show_EQs(self):
        eqsFactory = EQsFactory()

        eqs = eqsFactory.eqs

        for e in eqs:
            self.button = Button(self, text=f'{e.name}')
            self.button.pack(expand=True)
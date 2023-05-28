from tkinter import *

from behavioral.strategy import *
from functools import partial


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Strategy")
        self.geometry("640x480")

        self.cleanSound = CleanSound()
        self.keyScape = KeyScape(self.cleanSound)

        self.vintageSound = VintageSound()
        self.mellotron = Mellotron(self.vintageSound)

        l = Label(self, text='KeyScape')
        l.pack()
        self.button = Button(self, text='Play Sound', command=self.play_keyscape)
        self.button.pack(expand=True)

        l = Label(self, text='Mellotron')
        l.pack()
        self.button = Button(self, text='Play Sound', command=self.play_mellotron)
        self.button.pack(expand=True)

        l = Label(self, text='Change to clean sound system')
        l.pack()
        self.button = Button(self, text='Change Sound System', command=partial(self.change_sound_system, self.mellotron, self.cleanSound))
        self.button.pack(expand=True)


    def play_keyscape(self):
        self.keyScape.playSound()

    def play_mellotron(self):
        self.mellotron.playSound()

    def change_sound_system(self, mellotron, cleanSound):
        mellotron.soundSystem = cleanSound
        mellotron.playSound()
from abc import ABCMeta, abstractmethod


class Sound(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        pass

class CleanSound(Sound):
    def sound(self):
        print("Clean sound")

class VintageSound(Sound):
    def sound(self):
        print("Vintage sound")

class Synth(metaclass=ABCMeta):
    def __init__(self, soundSystem):
        self._soundSystem = soundSystem

    def playSound(self):
        self._soundSystem.sound()

    @property
    def soundSystem(self):
        return self._soundSystem
    
    @soundSystem.setter
    def soundSystem(self, soundSystem):
        self._soundSystem = soundSystem


class KeyScape(Synth):
    def __init__(self, cleanSound):
        self.cleanSound = cleanSound
        super().__init__(cleanSound)

class Mellotron(Synth):
    def __init__(self, vintageSound):
        self.vintageSound = vintageSound
        super().__init__(vintageSound)

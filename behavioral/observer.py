class Observable:
    def __init__(self):
        self.observers = []

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)


class Compressor(Observable):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._gain = 0

    @property
    def gain(self):
        return self._gain
    
    @gain.setter
    def setGain(self, value):
        self._gain = value
        self.notify()
        


class Kick:
    def __init__(self):
        self._name = "Kick"

    def update(self, subject):
        print('Kick: Subject %s has data: gain %d' % (subject.name, subject.setGain))


    @property
    def name(self):
        return self._name
from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):
    @abstractmethod
    def type():
        raise NotImplementedError
    

class EffectPlugin(Plugin):
    def __init__(self):
        self.type = "Effect"

    def type(self):
        return self.type


class SynthPlugin(Plugin):
    def __init__(self):
        self.type = "Synth"

    def type(self):
        return self.type

class Creator:
    @staticmethod
    def Factory(type):
        if type == 'Effect':
            return EffectPlugin()
        elif type == 'Synth':
            return SynthPlugin()
        return None
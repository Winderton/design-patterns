
from tkinter import *
from structural.decorator import *
 

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Decorator")
        self.geometry("1280x200")
        self.dry = Entity("sound")
          
        l = Label(self, bg='white', width=30, text=self.dry.play())
        l.pack()
        
        def result():
            if (comp.get()) and (not eq.get()):
                wet = Compressor(self.dry)
                l.config(text=wet.play())
            elif (not comp.get()) and (eq.get()):
                wet = EQ(self.dry)
                l.config(text=wet.play())
            elif (comp.get()) and (eq.get()):
                wet = EQ(Compressor(self.dry))
                l.config(text=wet.play())
            else:
                l.config(text=self.dry.play())
        
        comp = IntVar(value=0)
        eq = IntVar(value=0)
        first = Checkbutton(self, text='Compressor',variable=comp, command=result)
        first.pack()
        second = Checkbutton(self, text='EQ',variable=eq, command=result)
        second.pack()





    

from tkinter import *
from creational.singleton import Singleton
import eqswindow
import footerwindow
import converterwindow
import decoratorwindow
import renderwindow
import iteratorwindow
import groupwindow
import strategywindow

class Window(Tk, Singleton):
    def init(self):
        print('calling from init')
        super().__init__()

    
        self.button = Button(self, text='open eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)

        self.button = Button(self, text='open footer', command=self.create_footer_eqs)
        self.button.pack(expand=True)

        self.button = Button(self, text='converter', command=self.create_converter_window)
        self.button.pack(expand=True)

        self.button = Button(self, text='decorator', command=self.create_decorator_window)
        self.button.pack(expand=True)

        self.button = Button(self, text='export', command=self.create_export_window)
        self.button.pack(expand=True)

        self.button = Button(self, text='iterator', command=self.create_iterator_window)
        self.button.pack(expand=True)

        self.button = Button(self, text='sampler', command=self.create_group_window)
        self.button.pack(expand=True) 

        self.button = Button(self, text='strategy', command=self.create_strategy_window)
        self.button.pack(expand=True) 


    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqswindow.Extra()

    def create_footer_eqs(self):
        global extraWindow
        extraWindow = footerwindow.Extra()

    def create_converter_window(self):
        global extraWindow
        extraWindow = converterwindow.Extra()

    def create_decorator_window(self):
        global extraWindow
        extraWindow = decoratorwindow.Extra()

    def create_export_window(self):
        global extraWindow
        extraWindow = renderwindow.Extra()

    def create_iterator_window(self):
        global extraWindow
        extraWindow = iteratorwindow.Extra()

    def create_group_window(self):
        global extraWindow
        extraWindow = groupwindow.Extra()

    def create_strategy_window(self):
        global extraWindow
        extraWindow = strategywindow.Extra()


    
    def __init__(self):
        print('calling from __init__')
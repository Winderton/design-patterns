from mainwindow import Window

class Eq:
    pass

class uadED(Eq):
    pass

class wavesEQ(Eq):
    pass




if __name__ == "__main__":

    first = uadED()
    second = wavesEQ()

    
    handle = Window()
    handle2 = Window()
    handle2.title('Daw2')
    handle.title('Daw')
    handle2.geometry('1280x720')
    handle.geometry('1280x720')

    assert(handle is handle2)

    handle2.mainloop()
    handle.mainloop()

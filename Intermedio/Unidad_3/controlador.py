from tkinter import *
from vista import Ventanita

class Controller:

    def __init__(self, root):
        self.root_controler=root
        self.objeto_vista=Ventanita(self.root_controler)


if __name__=="__main__":
    root=Tk()
    mi_app=Controller(root)
    root.mainloop()
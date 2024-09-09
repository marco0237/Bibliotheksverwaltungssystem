from tkinter import NSEW, Button, Frame
from shared.utils import create_PlaceHolder


class AboutView(Frame):

    def __init__(self):
        super().__init__()
        self.title = "About"
        self.__initUI__()

    def __initUI__(self):
        self.placeHolder = create_PlaceHolder(
            self, "ABOUT --- Implementation is coming ...!")
        self.placeHolder.grid(row=0, column=1)

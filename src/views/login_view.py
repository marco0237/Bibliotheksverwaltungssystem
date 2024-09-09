from tkinter import NSEW, Button, Frame
from shared.utils import createPlaceHolder


class LoginView(Frame):
    def __init__(self):
        super().__init__()
        self.title = "Login"
        self.__initUI__()

    def __initUI__(self):
        self.placeHolder = createPlaceHolder(
            self, "LoGIN --- Implementation is coming ...!")
        self.placeHolder.grid(row=0, column=1)

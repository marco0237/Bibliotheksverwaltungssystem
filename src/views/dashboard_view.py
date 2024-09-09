from tkinter import NSEW, Button, Frame

from shared.utils import create_PlaceHolder


class DashboardView(Frame):
    def __init__(self):
        super().__init__()
        self.title = "Dashboard"
        # Fixed width for column 1
        self.grid_columnconfigure(0, weight=0, minsize=10)
        self.grid_columnconfigure(1, weight=1)  # Column 2 will stretch
        self.__initUI__()

    def __initUI__(self):
        self.placeHolder = create_PlaceHolder(
            self, "ABOUT --- Implementation is coming ...!")
        self.grid(row=0, column=0, sticky=NSEW)
        self.b1 = Button(self, text="DashboardView")
        self.b1.grid(row=0, column=1)

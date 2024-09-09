from tkinter import NSEW, Button, Frame

from shared.constants import BG_COLOR, BG_FRAME_COLOR
from shared.utils import createPlaceHolder


class DashboardView(Frame):
    def __init__(self):
        super().__init__()
        self.title = "Dashboard"
        self.configure(bg=BG_FRAME_COLOR)
        # Fixed width for column 1
        self.grid_columnconfigure(0, weight=0, minsize=10)
        self.grid_columnconfigure(1, weight=1)  # Column 2 will stretch
        self.__initUI__()

    def __initUI__(self):
        self.placeHolder = createPlaceHolder(
            self, "DASH --- Implementation is coming ...!")
        self.placeHolder.grid(row=0, column=0, sticky=NSEW)

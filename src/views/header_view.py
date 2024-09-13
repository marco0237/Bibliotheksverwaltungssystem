

from tkinter import NSEW, Frame
from shared.constants import BG_FRAME_COLOR
from shared.utils import createHeader


class HeaderView(Frame):

    def __init__(self, text: str):
        super().__init__()

        self.configure(bg=BG_FRAME_COLOR)
        self.grid_rowconfigure(0, weight=1, minsize=10)
        self.grid_columnconfigure(0, weight=1, minsize=10)

        self.__initUI__(text)

    def __initUI__(self, text) -> None:
        self.label = createHeader(self, text)
        self.label.configure(background=BG_FRAME_COLOR)
        self.label.grid(row=0, column=0, sticky=NSEW, ipadx=0)

    def update_header(self, newt_ext: str) -> None:
        self.label.configure(text=newt_ext)

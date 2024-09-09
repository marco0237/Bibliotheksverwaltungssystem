from tkinter import Entry, Frame

from shared.utils import create_PlaceHolder


class BooksView(Frame):
    def __init__(self):
        super().__init__()
        self.title = "Books"
        self.__initUI__()

    def __initUI__(self):
        self.placeHolder = create_PlaceHolder(
            self, "Books --- Implementation is coming ...!")
        self. placeHolder.grid(row=0, column=1)

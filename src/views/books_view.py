from tkinter import Entry, Frame


class BooksView(Frame):
    def __init__(self):
        super().__init__()
        self.title = "Books"
        self.entry= Entry(width=100)
        self.grid(row=1, column=1)

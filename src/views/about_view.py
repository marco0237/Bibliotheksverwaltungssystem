from tkinter import Button, Frame


class AboutView(Frame):

    def __init__(self):
        super().__init__()
        self.title = "About"
        self.b1 = Button(text="About")
        self.b1 .grid(row=0,column=0)

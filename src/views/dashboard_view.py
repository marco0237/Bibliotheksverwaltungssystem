from tkinter import Button, Frame


class DashboardView(Frame):
    def __init__(self):
        super().__init__()
        self.title = "Dashboard"
        self.b1 = Button(text="DashboardView")
        self.b1 .grid(row=0,column=0)

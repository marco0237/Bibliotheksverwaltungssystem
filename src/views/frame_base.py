from tkinter import Frame


class FrameBase (Frame): # inheritance
    def __init__(self):
        super().__init__()
        self.title = ""
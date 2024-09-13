from tkinter import Frame

from docutils.nodes import title


class FrameBase (Frame): # Vererbung
    def __init__(self):
        super().__init__()
        self.title = ""
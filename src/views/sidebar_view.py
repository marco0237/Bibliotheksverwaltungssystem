
from tkinter import Button, Frame
from typing import List


class SidebarView(Frame):
    def __init__(self, buttons: List[Button]):
        super().__init__()
        for btn in buttons:

            self.sidebarBtn.grid(row=0, column=0)

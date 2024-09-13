from tkinter.font import Font

from shared.constants import BG_FRAME_COLOR

from src.views.frame_base import FrameBase


class MembersView(FrameBase):
    def __init__(self):
        super().__init__()
        self.title = "Members"
        self.configure(bg=BG_FRAME_COLOR)
        # Fixed width for column 1
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)  # Column 2 will stretch
        self.grid_columnconfigure(2, weight=0)  # Column 2 will stretch
        self.grid_columnconfigure(3, weight=0)  # Column 2 will stretch
        self.grid_columnconfigure(3, weight=1)  # Column 2 will stretch

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(2, weight=1)  # Column 2 will stretch

        self.stringFont = Font(family="Helvetica", size=26, weight="bold")
        self.numberFont = Font(
            family="Montserrat Bold",
            size=36,
            weight="bold")

        self.__initUI__()

    def __initUI__(self) -> None:
        pass

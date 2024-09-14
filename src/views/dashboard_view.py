from pathlib import Path
from tkinter import Frame
from tkinter.font import Font
# from customtkinter import CTk, CTkCheckBox, CTkButton, CTkFrame, CTkLabel
from controllers.main_controller import MainController
from shared.constants import ASSETS_PATH, BG_FRAME_COLOR
from shared.utils import create_header_label, create_count_label, create_label_image
from views.frame_base import FrameBase


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class DashboardView(FrameBase):
    def __init__(self, master, controller: MainController, **kwargs):
        super().__init__(master, **kwargs)
        self.title = "Dashboard"
        self.controller = controller

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

        self.update_ui()

    def __initUI__(self) -> None:

        # Borrowed
        borrowed_frame = Frame(self, padx=1, pady=1)
        borrowed_frame.grid(row=0, column=0)
        borrowed_label = create_header_label(
            borrowed_frame, "Borrowed", self.stringFont)
        borrowed_label.grid(row=0, column=0)
        self.borrowedValueLabel = create_count_label(
            borrowed_frame, "350", self.numberFont)
        self.borrowedValueLabel.grid(row=1, column=1)

        # Member
        members_frame = Frame(self, padx=50, pady=1)
        members_frame.grid(row=0, column=1)
        member_label = create_header_label(
            members_frame, "Members", self.stringFont)
        member_label.grid(row=0, column=0)
        self.membersValueLabel = create_count_label(
            members_frame, "4.1k", self.numberFont)
        self.membersValueLabel.grid(row=1, column=1)

        # Available Books
        available_books_frame = Frame(self, padx=1, pady=1)
        available_books_frame.grid(row=1, column=0)
        available_books_label = create_header_label(
            available_books_frame, "Avail.Books", self.stringFont)
        available_books_label.grid(row=0, column=0)
        self.availableBooksValueLabel = create_count_label(
            available_books_frame, "311b", self.numberFont)
        self.availableBooksValueLabel.grid(row=1, column=1)

        # Boy

    def update_ui(self):
        print(f"===================== {type(self.controller)}")
        self.membersValueLabel.configure(
            text=len(self.controller.load_member()))

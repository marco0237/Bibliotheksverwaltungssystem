from pathlib import Path
from tkinter import NSEW, Button, Checkbutton, Frame, Label, LabelFrame, PhotoImage
from tkinter.font import Font


from shared.constants import ASSETS_PATH, BG_COLOR, BG_FRAME_COLOR, OUTPUT_PATH
from shared.utils import createButonImage, createCountLabel, createHeader, createHeaderLabel, createLabelImage, createPlaceHolder


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class DashboardView(Frame):
    def __init__(self):
        super().__init__()
        self.title = "Dashboard"
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

        # Borrowed
        borrowedFrame = Frame(self, padx=1, pady=1)
        borrowedFrame.grid(row=0, column=0)
        borrowedLabel = createHeaderLabel(
            borrowedFrame, "Borrowed", self.stringFont)
        borrowedLabel.grid(row=0, column=0)
        self.borrowedValueLabel = createCountLabel(
            borrowedFrame, "350", self.numberFont)
        self. borrowedValueLabel.grid(row=1, column=1)

        # Member
        membersFrame = Frame(self, padx=50, pady=1)
        membersFrame.grid(row=0, column=1)
        memberLabel = createHeaderLabel(
            membersFrame, "Members", self.stringFont)
        memberLabel.grid(row=0, column=0)
        self.membersValueLabel = createCountLabel(
            membersFrame, "4.1k", self.numberFont)
        self.membersValueLabel.grid(row=1, column=1)

       # Available Books
        availableBooksFrame = Frame(self, padx=1, pady=1)
        availableBooksFrame.grid(row=1, column=0)
        availableBooksLabel = createHeaderLabel(
            availableBooksFrame, "Avai. Books", self.stringFont)
        availableBooksLabel.grid(row=0, column=0)
        self.availableBooksValueLabel = createCountLabel(
            availableBooksFrame, "11k", self.numberFont)
        self.availableBooksValueLabel.grid(row=1, column=1)

        # Boy
        boyFrame = Frame(self, padx=1, pady=52)
        boyFrame.grid(row=1, column=1)
        photoImage = PhotoImage(file=relative_to_assets("boy.png"))
        labelImage = createLabelImage(
            boyFrame, photo=photoImage)
        labelImage.image = photoImage
        labelImage.grid(row=0, column=0)  # place it

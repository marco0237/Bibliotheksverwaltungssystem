from pathlib import Path
from tkinter import NSEW, Button, Frame, Label, PhotoImage, StringVar
from tkinter.font import Font

from shared.constants import BG_COLOR, FG_COLOR, FG_VIEW_COLOR


# -----------  Global methods  ---------------------
def createPlaceHolder(parent, text) -> Label:
    return Label(
        parent,
        text=text,
        font=(
            "Montserrat Bold",
            36 * -1))


def createHeader(parent, text) -> Label:
    return Label(
        parent,
        text=text,
        foreground=FG_VIEW_COLOR,
        font=(
            "Montserrat Bold",
            26 * -1))


def createLogoHeader(parent, text) -> Label:
    return Label(
        parent,
        fg="white",
        bg=BG_COLOR,
        text=text,
        font=(
            "Montserrat Bold",
            36 * -1))


def createCountLabel(parent, text, font: Font) -> Label:
    return Label(
        parent,
        text=text,
        foreground=FG_VIEW_COLOR,
        font=font)


def createHeaderLabel(parent, text, font: Font) -> Label:
    return Label(
        parent,
        text=text,
        foreground=FG_VIEW_COLOR,
        font=font)


def createButonImage(parent, fileImage) -> Button:

    button_image_1 = PhotoImage(file=fileImage)
    return Button(
        parent,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        # command=lambda: self.handle_btn_press(self.dashboard_btn, "dash"),
        cursor='hand2',
        activebackground="#5E95FF",
        relief="flat",
    )


def createLabelImage(parent, photo) -> Label:

     
    return Label(
        parent,
        image=photo,
        borderwidth=0,
        highlightthickness=0,
        cursor='hand2',
        activebackground="#5E95FF",
        relief="flat",
    )

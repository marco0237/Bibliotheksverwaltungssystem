from tkinter import NSEW, Frame, Label

from shared.constants import BG_COLOR, FG_COLOR, FG_VIEW_COLOR


def createPlaceHolder(parent, text) -> Label:
    return Label(
        parent,
        text=text,
        font=(
            "Montserrat Bold",
            36 * -1))


def createHeader(parent, text) -> Frame:

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

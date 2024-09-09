from tkinter import Label

from shared.constants import BG_COLOR, FG_COLOR


def create_PlaceHolder(parent, text) -> Label:

    return Label(
        parent,
        fg=FG_COLOR,
        bg=BG_COLOR,
        text=text,
        font=(
            "Montserrat Bold",
            36 * -1))

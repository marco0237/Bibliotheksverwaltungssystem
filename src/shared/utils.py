from pathlib import Path
from tkinter import Button, Label, PhotoImage
from tkinter.font import Font
# from customtkinter import CTkLabel
from shared.constants import ASSETS_PATH, BG_COLOR, FG_VIEW_COLOR

# ------------------------- GLOBAL METHODS -------------------------------


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_place_holder(parent, text) -> Label:
    return Label(
        parent,
        text=text,
        font=(
            "Montserrat Bold",
            36 * -1))


def create_header(parent, text) -> Label:
    return Label(
        parent,
        text=text,
        foreground=FG_VIEW_COLOR,
        font=(
            "Montserrat Bold",
            26 * -1))


def create_logo_header(parent, text) -> Label:
    return Label(
        parent,
        fg="white",
        bg=BG_COLOR,
        text=text,
        font=(
            "Montserrat Bold",
            36 * -1))


def create_count_label(parent, text, font: Font) -> Label:
    return Label(
        parent,
        text=text,
        foreground=FG_VIEW_COLOR,
        font=font)


def create_header_label(parent, text, font: Font) -> Label:
    return Label(
        parent,
        text=text,
        foreground=FG_VIEW_COLOR,
        font=font)


def create_button_image(parent, file_image) -> Button:

    button_image_1 = PhotoImage(file=file_image)
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


def create_label_image(parent, photo) -> Label:

    return Label(
        parent,
        image=photo,
        borderwidth=0,
        highlightthickness=0,
        cursor='hand2',
        bg="white",
        activebackground="#5E95FF",
        relief="flat",
    )

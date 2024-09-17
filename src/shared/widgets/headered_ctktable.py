
from CTkTable import *    # https://github.com/Akascape/CTkTable


class HeaderedCTkTable(CTkTable):
    """ Headered CTkTable Widget """

    def __init__(
            self,
            master: any,
            headers: list,
            row: int = None,
            column: int = None,
            padx: int = 1,
            pady: int = 0,
            width: int = 140,
            height: int = 28,
            values: list = None,
            colors: list = [None, None],
            orientation: str = "horizontal",
            color_phase: str = "horizontal",
            border_width: int = 0,
            text_color=None,
            border_color=None,
            font: tuple = None,
            header_color=None,
            corner_radius: int = 25,
            write: str = False,
            command=None,
            anchor: str = "c",
            hover_color=None,
            hover: bool = False,
            justify: str = "center",
            wraplength: int = 1000,
            **kwargs):

        super().__init__(master, row, column, padx, pady, width,
                         height,
                         values,
                         colors,
                         orientation,
                         color_phase,
                         border_width,
                         text_color,
                         border_color,
                         font,
                         header_color,
                         corner_radius,
                         write,
                         command,
                         anchor,
                         hover_color,
                         hover,
                         justify,
                         wraplength,
                         kwargs)

        if headers is None:
            headers = []

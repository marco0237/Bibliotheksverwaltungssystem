
# from CTkTable import *    # https://github.com/Akascape/CTkTable
from customtkinter import CTkLabel, CTkFrame


class HeaderedCTkTable(CTkFrame):
    """ Headered CTkTable Widget """

    def __init__(self, master, data, headers=None,
                 row_height=30, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.data = data
        self.headers = headers
        self.row_height = row_height

        self.grid_columnconfigure(list(range(len(data[0]))), weight=1)

        if headers:
            self._create_headers()
        self._create_rows()

    def _create_headers(self):
        """Create the table headers."""
        for col_num, header in enumerate(self.headers):
            label = CTkLabel(
                self,
                text=header,
                fg_color="gray",
                corner_radius=5,
                height=self.row_height)
            label.grid(row=0, column=col_num, sticky="nsew", padx=2, pady=2)

    def _create_rows(self):
        """Create the table rows with data."""
        start_row = 1 if self.headers else 0
        for row_num, row_data in enumerate(self.data, start=start_row):
            for col_num, cell_data in enumerate(row_data):
                label = CTkLabel(
                    self,
                    text=cell_data,
                    fg_color="white",
                    height=self.row_height)
                label.grid(
                    row=row_num,
                    column=col_num,
                    sticky="nsew",
                    padx=2,
                    pady=2)

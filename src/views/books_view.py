from customtkinter import CTkCheckBox, CTkButton, CTkLabel, CTkProgressBar, CTkSwitch, CTkComboBox, CTkSegmentedButton
from views.frame_base import FrameBase


class BooksView(FrameBase):

    def __init__(self, master, **kwargs):
        super().__init__(master, "Books", **kwargs)
        self.__initUI__()

    def __initUI__(self):

        button = CTkButton(self, text="Add Book", command=self.button_function)
        button.grid(row=0, column=0)

        chekcbok = CTkCheckBox(self, text="Add Book")
        chekcbok.grid(row=1, column=1)

        labele = CTkLabel(self, text="Je suis un label")
        labele.grid(row=1, column=2)

        progress = CTkProgressBar(
            self,
            indeterminate_speed=10,
            mode="indeterminate",
            width=500,
            height=20)
        progress.grid(row=3, column=3)

        switch = CTkSwitch(
            self,
            text="CTkSwitch",
            onvalue="on",
            offvalue="off")
        switch.grid(row=4, column=3)

        combobox = CTkComboBox(self, values=["ABCDE 1", "DFRDS 2"])
        combobox.grid(row=5, column=3)

        segemented_button = CTkSegmentedButton(
            self, values=["Value 1", "Value 2", "Value 3", "Ghislain"])
        segemented_button.grid(row=6, column=3)

    def button_function(self):
        print("someone clicks on  Add Book !!--")

    def update_ui(self):
        pass

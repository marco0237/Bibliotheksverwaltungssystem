from tkinter import StringVar
from tkinter.font import Font
from services.member_service import MemberService
from views.frame_base import FrameBase
from customtkinter import CTkScrollableFrame, CTkRadioButton
import asyncio
from CTkTable import *


class ScrollableRadiobuttonFrame(CTkScrollableFrame):
    def __init__(self, master, item_list: list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_variable = StringVar()
        self.radiobutton_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        radiobutton = CTkRadioButton(
            self,
            text=item,
            value=item,
            variable=self.radiobutton_variable)
        if self.command is not None:
            radiobutton.configure(command=self.command)
        radiobutton.grid(
            row=len(
                self.radiobutton_list), column=0, pady=(
                0, 10))
        self.radiobutton_list.append(radiobutton)

    def remove_item(self, item):
        for radiobutton in self.radiobutton_list:
            if item == radiobutton.cget("text"):
                radiobutton.destroy()
                self.radiobutton_list.remove(radiobutton)
                return

    def get_checked_item(self):
        return self.radiobutton_variable.get()


class MembersView(FrameBase):
    def __init__(self, master, service: MemberService):
        super().__init__(master)
        self.title = "Members"
        self.service = service

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

        self.__initUI__()

    def __initUI__(self) -> None:
        
        # self.service.print_members()
        asyncio.run(self.service.print_members_async())
        members = asyncio.run(self.service.get_members_async())

        # https://github.com/Akascape/CTkTable
        table = CTkTable(master=self, column=5, values=members)
        table.grid(row=0, column=1, padx=15, pady=15, sticky="ns")

    def radiobutton_frame_event(self):
        print(
            f"radiobutton frame modified: {
                self.scrollable_radiobutton_frame.get_checked_item()}")

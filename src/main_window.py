
from tkinter import END, NSEW, Button, Frame, Label, Text, Tk
from typing import List

from controllers.main_controller import MainController
from models.user_model import UserModel
from shared.constants import BG_COLOR, FG_COLOR
from shared.utils import createHeader, createLogoHeader
from views.about_view import AboutView
from views.dashboard_view import DashboardView
from views.books_view import BooksView
from views.header_view import HeaderView
from views.login_view import LoginView
from views.sidebar_view import SidebarView


# ----Constants -------

LOGIN_KEY = "login"
HEAD_TITLE = "MarcoGo"


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.model = UserModel()
        self.title('The State of LMS')
        self.controller = None
        self.geometry("1012x506")
        # self.configure(bg=BG_COLOR)
        # Fixed width for column 1
        self.grid_columnconfigure(0, weight=0, minsize=5)
        self.grid_columnconfigure(1, weight=1)  # Column 2 will stretch

        self.grid_rowconfigure(0, weight=0, minsize=10)
        self.grid_rowconfigure(1, minsize=10)

        self.__frames__: dict[str, Frame] = {
            "dash": DashboardView(),
            "about": AboutView(),
            "books": BooksView(),
            "login": LoginView(),

        }
        self.__initUI__()

    def __initUI__(self):

        # Head of app
        headingLogo = createLogoHeader(self, HEAD_TITLE)
        headingLogo.grid(row=0, column=0, ipadx=10, ipady=10, sticky=NSEW,)

        # Header of selected frame
        self.headerFrame = HeaderView(" ")
        self.headerFrame.grid(
            row=0,
            column=1,
            ipadx=10,
            ipady=10,
            sticky=NSEW,
        )

        # Sidebar elements
        self.sideBar = Frame(bg=BG_COLOR, padx=1, pady=1)
        self.sideBar.grid(row=1, column=0, sticky=NSEW)
        rowIndex = 0
        for (key, item) in self.__frames__.items():
            self.__createSidebarButton__(
                self.sideBar, item.title, key).grid(
                row=rowIndex, column=0, pady=50, padx=1)
            rowIndex += 1

        # Hide all self.__frames__
        for frame in self.__frames__.values():
            frame.grid_forget()

        # Show only dashbord
        self.onSidebarBtnClicked("dash")

    def onSidebarBtnClicked(self, keyOfFrame):
        # Place the sidebar on respective button
        # self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for frame in self.__frames__.values():
            frame.grid_forget()

        self.selectedFrame = self.__frames__.get(keyOfFrame)

        # Show the frame of the button clicked
        self.selectedFrame.grid(
            row=1,
            column=1,
            ipady=10,
            pady=2,
            padx=4,
            sticky=NSEW)

        # Handle label change
        current_name = self.__frames__.get(
            keyOfFrame)._name.split("!")[-1].capitalize()
        print(self.selectedFrame.title)
        # self.grid.itemconfigure(self.headingLabel, text=current_name)
        self.headerFrame.updateHeader(self.selectedFrame.title.capitalize())

    def __createSidebarButton__(
            self, parent: Frame, content: str, key: str) -> Button:
        bt = Button(
            parent,
            # image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.onSidebarBtnClicked(key),
            cursor='hand2',
            activebackground="#5E95FF",
            relief="flat",
            bg=BG_COLOR,
            name=key,
            fg=FG_COLOR,
            text=content,
        )
        return bt

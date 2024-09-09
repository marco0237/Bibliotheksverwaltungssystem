
from tkinter import END, NSEW, Button, Frame, Label, Text, Tk
from typing import List

from controllers.main_controller import MainController
from models.user_model import UserModel
from shared.constants import BG_COLOR, FG_COLOR
from views.about_view import AboutView
from views.dashboard_view import DashboardView
from views.books_view import BooksView
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
        self.configure(bg=BG_COLOR)
        # Fixed width for column 1
        self.grid_columnconfigure(0, weight=0, minsize=5)
        self.grid_columnconfigure(1, weight=1)  # Column 2 will stretch

        self.grid_rowconfigure(0, weight=0, minsize=10)
        self.grid_rowconfigure(
            1, weight=0, minsize=10)  # Column 2 will stretch
        # self.grid_rowconfigure(2, weight=0, minsize=10)  # for logout place

        self.initUi()

    def initUi(self):

        # Head of app
        headingLabel = Label(
            self,
            fg="white",
            bg=BG_COLOR,
            text=HEAD_TITLE,
            font=(
                "Montserrat Bold",
                36 * -1))
        # sticky="nsew" ==> stretch the widget
        headingLabel.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

        self.frames: dict[str, Frame] = {
            "dash": DashboardView(),
            "about": AboutView(),
            "books": BooksView(),
        }

        self.sideBar = Frame(bg=BG_COLOR, padx=1, pady=1)
        self.sideBar.grid(row=1, column=0)
        rowIndex = 0
        for (key, item) in self.frames.items():
            self.__createSidebarButton__(
                self.sideBar, item.title, key).grid(
                row=rowIndex, column=0, pady=50, padx=1)
            # item.grid(row=0, column=1, pady=10, padx=1)
            rowIndex += 1

        # Login/ Logout Button
        self.loginFrame = LoginView()
        loginBtn = self.__createSidebarButton__(
            self.sideBar, self.loginFrame.title, LOGIN_KEY)
        loginBtn.grid(row=len(self.frames),
                      column=0,
                      ipady=10,
                      pady=10,
                      padx=5)
        self.loginFrame.grid_forget()

        # Hide all frames
        for frame in self.frames.values():
            frame.grid_forget()

        # Show only dashbord
        self.selectedFrame = self.frames.get("dash")
        self.selectedFrame.grid(row=1, column=1)

    def onSidebarBtnClicked(self, keyOfFrame):
        # Place the sidebar on respective button
        # self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for frame in self.frames.values():
            frame.grid_forget()

        if keyOfFrame is LOGIN_KEY:
            self.selectedFrame = self.loginFrame
        else:
            self.loginFrame.grid_forget()
            # Set cucrrent Frame
            self.selectedFrame = self.frames.get(keyOfFrame)

        # Show the frame of the button clicked
        self.selectedFrame.grid(row=1, column=1, ipady=10, pady=10, padx=5)

        # Handle label change
        # current_name = self.windows.get(name)._name.split("!")[-1].capitalize()
        # self.canvas.itemconfigure(self.heading, text=current_name)

    def save_button_clicked(self):
        pass

    def getContent(self):
        pass

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

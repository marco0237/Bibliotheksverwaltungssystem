
from tkinter import Button, Frame, Label, Tk
from typing import List

from controllers.main_controller import MainController
from models.user_model import UserModel
from views.about_view import AboutView
from views.dashboard_view import DashboardView
from views.books_view import BooksView
from views.sidebar_view import SidebarView


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.model = UserModel()
        self.title('The State of LMS')
        self.controller = None
        self.geometry("1012x506")
        self.configure(bg="#5E95FF")
        # Fixed width for column 1
        self.grid_columnconfigure(0, weight=0, minsize=10)
        self.grid_columnconfigure(1, weight=1)  # Column 2 will stretch

        self.initUi()

    def initUi(self):

        self.frames:dict[str,Frame] = {
            "dash": DashboardView(),
            "about": AboutView(),
            "books": BooksView(),
        }

        self.sideBar = Frame(bg="red", padx=15, pady=15)
        self.sideBar.grid(row=0, column=0)
        rowIndex = 0
        for (key, item) in  self.frames.items():
            self.__createSidebarButton__(
                self.sideBar, item.title, key).grid(
                row=rowIndex, column=0)
            rowIndex += 1

        self.selectedFrame = self.frames.get("dash")
        self.selectedFrame.grid(row=0, column=1)
        

    def onSidebarBtnClicked(self, caller, name):
        # Place the sidebar on respective button
        # self.sidebar_indicator.place(x=0, y=caller.winfo_y())   

        # Hide all screens
        for frame in  self.frames.values():
             frame.place_forget()

        # Set ucrrent Window
        self.selectedFrame = self.frames.get(name)
        print(self.selectedFrame)

        # Show the screen of the button pressed
        self.selectedFrame.grid(row=0, column=0)
        

        # Handle label change
        # current_name = self.windows.get(name)._name.split("!")[-1].capitalize()
        # self.canvas.itemconfigure(self.heading, text=current_name)

    def save_button_clicked(self):
        pass

    def getContent(self):
        pass

    def __createSidebarButton__(
            self, parent, content: str, key: str) -> Button:
        btn = Button(
            parent,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2', 
            activebackground="#5E95FF",
            relief="flat",
            width=50,
            height=10,
            name=key,
            text=content,
            command=lambda: self.onSidebarBtnClicked(btn, key)
        )
        return btn

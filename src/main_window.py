from tkinter import NSEW, Frame
from customtkinter import CTk, CTkButton

from controllers.main_controller import MainController
from models.user_model import UserModel
from services.member_service import MemberService
from shared.constants import BG_COLOR
from shared.utils import create_logo_header
from views.frame_base import FrameBase
from views.about_view import AboutView
from views.dashboard_view import DashboardView
from views.books_view import BooksView
from views.header_view import HeaderView
from views.login_view import LoginView
from views.members_view import MembersView

# ----Constants -------
LOGIN_KEY = "login"
HEAD_TITLE = "MarcoGo"


class MainWindow(CTk):

    def __init__(self, controller: MainController, *args, **kwargs):
        super().__init__(**kwargs)
        print(args)
        self.model = UserModel()
        self.title('The State of LMS')
        self.controller = controller
        self.geometry("1012x506")
        # self.iconbitmap(relative_to_assets("boy.xbm"))
        self.selectedFrame = None
        # self.configure(bg=BG_COLOR)
        # Fixed width for column 1
        self.grid_columnconfigure(0, weight=0, minsize=5)
        self.grid_columnconfigure(1, weight=1)  # Column 2 will stretch

        self.grid_rowconfigure(0, weight=0, minsize=10)
        self.grid_rowconfigure(1, minsize=10, weight=0)
        self.grid_rowconfigure(1, minsize=10, weight=1)

        self.__frames__: dict[str, FrameBase] = {
            "dash": DashboardView(master=self, controller=controller, **kwargs),
            "members": MembersView(master=self, service=MemberService(controller)),
            "books": BooksView(master=self),
            "about": AboutView(master=self),
            "login": LoginView(master=self),

        }
        self.__initUI__()

    def __initUI__(self):

        # Head of app
        heading_logo = create_logo_header(self, HEAD_TITLE)
        heading_logo.grid(row=0, column=0, ipadx=10, ipady=10, sticky=NSEW,)

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
        self.sideBar = Frame(self, background=BG_COLOR)
        self.sideBar.grid(row=1, column=0, sticky=NSEW)
        row_index = 0
        for (key, item) in self.__frames__.items():
            print(f"==========={key}")
            sideBarBtn = CTkButton(self.sideBar, text=item.title,
                                   command=lambda argument=key: self.on_sidebar_btn_clicked(argument))

            sideBarBtn.grid(
                row=row_index, column=0, pady=0, padx=1, sticky=NSEW)
            row_index += 1

        # Hide all self.__frames__
        for frame in self.__frames__.values():
            frame.grid_forget()

        self.on_sidebar_btn_clicked("members")

    def on_sidebar_btn_clicked(self, key_of_frame):

        # Hide all screens
        for frame in self.__frames__.values():
            frame.grid_forget()

        self.selectedFrame = self.__frames__.get(key_of_frame)

        # Show the frame of the button clicked
        self.selectedFrame.grid(
            row=1,
            column=1,
            ipady=10,
            pady=2,
            padx=4,
            sticky=NSEW)

        # Handle label change
        # self.grid.itemconfigure(self.headingLabel, text=current_name)
        self.headerFrame.update_header(self.selectedFrame.title.capitalize())

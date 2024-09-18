from tkinter import BOTH, NSEW
from shared.constants import BG_COLOR
# from shared.utils import  relative_to_assets
from views.frame_base import FrameBase
from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkFont, CTkEntry, CTkImage


class LoginView(FrameBase):
    def __init__(self, master, controller=None):
        super().__init__(master)
        self.title = "Login"

        # grid 2x1
        self.grid_columnconfigure(0, weight=1, minsize=5)
        self.grid_columnconfigure(1, weight=1, minsize=10)
        self.grid_rowconfigure(0, weight=1, minsize=10)  # left, right

        self.__initUI__()

    def __initUI__(self):

        # left
        left_frame = CTkFrame(master=self, fg_color=BG_COLOR,)
        left_frame.grid(row=0, column=0, sticky=NSEW)
        # Boy
        # boy_path= relative_to_assets("boy.png")
        # boy_image = CTkImage(light_image=boy_path, size=(500, 150))
        # boy_label = CTkLabel(left_frame, text="", image=boy_image)

        # right
        right_frame = CTkFrame(master=self, fg_color="white")
        right_frame.grid(row=0, column=1, sticky=NSEW)
        details_label = CTkLabel(
            right_frame,
            text="Enter your login details",
            font=CTkFont(size=20, weight="bold"),
            text_color=BG_COLOR)
        details_label.pack(fill=BOTH)
        description_label = CTkLabel(
            right_frame,
            text="Enter the credentials that the admin gave\n you while signing up for the program")
        description_label.pack()
        self.__create_username(right_frame)
        self.__create_password(right_frame)
        self.__create_login_button(right_frame)

    def __create_username(self, container):
        frame = CTkFrame(container, width=300, height=350)
        frame.pack(pady=(20, 20))
        username_label = CTkLabel(
            frame,
            text="Username",
            font=CTkFont(size=15),
            text_color=BG_COLOR)
        username_label.pack(fill=BOTH)
        username_entry = CTkEntry(
            master=frame, placeholder_text="Enter Username")
        username_entry.pack(fill=BOTH)

    def __create_password(self, parent):
        frame = CTkFrame(master=parent, width=300, height=150, border_width=10)
        frame.pack(pady=(20, 20))
        pass_label = CTkLabel(
            frame,
            text="Password",
            font=CTkFont(size=15),
            text_color=BG_COLOR)
        pass_label.pack(fill=BOTH)
        password_entry = CTkEntry(master=frame, show="*", width=250)
        password_entry.pack(fill=BOTH)

    def __create_login_button(self, container: CTkFrame):
        login_button = CTkButton(
            container,
            text="Login",
            fg_color=BG_COLOR,
            round_height_to_even_numbers=True)
        login_button.pack(pady=(20, 20))

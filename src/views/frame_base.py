from abc import abstractmethod
from customtkinter import CTkFrame

from controllers.main_controller import MainController

# https://customtkinter.tomschimansky.com/documentation/widgets/frame


class FrameBase (CTkFrame):  # inheritance

    def __init__(self, master, title, **kwargs):
        super().__init__(master, **kwargs)
        self.title: str = title
        self.controller: MainController = None

    def set_controller(self, controller: MainController):
        self.controller = controller

    @abstractmethod
    def update_ui(self):
        pass

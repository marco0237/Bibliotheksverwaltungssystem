from shared.utils import create_place_holder

from views.frame_base import FrameBase


class LoginView(FrameBase):
    def __init__(self):
        super().__init__()
        self.title = "Login"
        self.__initUI__()

    def __initUI__(self):
        self.placeHolder = create_place_holder(
            self, "LoGIN --- Implementation is coming ...!")
        self.placeHolder.grid(row=0, column=1)

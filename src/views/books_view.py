from shared.constants import BG_FRAME_COLOR
from shared.utils import create_place_holder

from views.frame_base import FrameBase


class BooksView(FrameBase):
    def __init__(self):
        super().__init__()
        self.title = "Books"
        self.configure(bg=BG_FRAME_COLOR)
        self.__initUI__()

    def __initUI__(self):
        self.placeHolder = create_place_holder(
            self, "Books --- Implementation is coming ...!")
        self. placeHolder.grid(row=0, column=1)

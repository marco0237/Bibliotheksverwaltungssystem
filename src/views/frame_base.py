from customtkinter import CTkFrame

# https://customtkinter.tomschimansky.com/documentation/widgets/frame


class FrameBase (CTkFrame):  # inheritance
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title: str = None

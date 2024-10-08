from customtkinter import set_appearance_mode, set_default_color_theme

from controllers.main_controller import MainController
from main_window import MainWindow
from models.library import Library

# Modes: system (default), light, dark
set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
set_default_color_theme("blue")


class App:
    def __init__(self, *args, **kwargs):
        self.main_window = None

        # Open Main
        self.open_main_window(args, kwargs)

    def open_main_window(self, *args, **kwargs):
        if self.main_window is None or not self.main_window.winfo_exists():

            model = Library()  # MVC: Model
            view = MainWindow()  # MVC: View
            controller = MainController(model, view)  # MVC: Controller
            # create window if its None or destroyed
            self.main_window = view
            view.set_controller(controller)
            self.main_window.mainloop()

        else:
            self.main_window.focus()


# ----------------MAIN-------------------
if "__main__" == __name__:
    # create a view
    app = App()

from tkinter import Tk
import sqlite3  # https://docs.python.org/3/library/sqlite3.html
#from controllers.main_controller import MainController
#from main_window import MainWindow
from models.user_model import UserModel
from src.controllers.main_controller import MainController
from src.main_window import MainWindow

# ----------------MAIN-------------------
if "__main__" == __name__:
    # model = Model()
    # view = View()
    controller = MainController()
    # view.mainloop()

    # create a view
    mainView = MainWindow(controller)
    mainView.mainloop()

from tkinter import Tk

from controllers.main_controller import MainController
from main_window import MainWindow
from models.user_model import UserModel
# ----------------MAIN-------------------
if "__main__" == __name__:
    # model = Model()
    # view = View()
    # controller = ViewModel(model, view)
    # view.mainloop()

    # create a view
    mainView = MainWindow()
    mainView.mainloop()

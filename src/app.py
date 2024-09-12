#from controllers.main_controller import MainController
#from main_window import MainWindow
from controllers.main_controller import MainController
from main_window import MainWindow

# ----------------MAIN-------------------
if "__main__" == __name__:
    # model = Model()
    # view = View()
    controller = MainController()
    # view.mainloop()

    # create a view
    mainView = MainWindow(controller)
    mainView.mainloop()

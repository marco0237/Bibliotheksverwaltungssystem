from tkinter import NSEW, Canvas
from shared.utils import create_place_holder

from views.frame_base import FrameBase


class AboutView(FrameBase):

    def __init__(self):
        super().__init__()
        self.canvas = None
        self.title = "About"
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.__initUI__()

    def __initUI__(self):
        self.placeHolder = create_place_holder(
            self, "ABOUT --- Implementation is coming ...!")
        self.placeHolder.grid(row=1, column=1)
        self.demo_grid()

    @staticmethod
    def create_grid(canvas, width, height, rows, columns):
        # Calculate the size of each cell
        cell_width = width // columns
        cell_height = height // rows

        # Draw vertical lines
        for col in range(columns + 1):
            x = col * cell_width
            canvas.create_line(x, 0, x, height, fill="black")

        # Draw horizontal lines
        for row in range(rows + 1):
            y = row * cell_height
            canvas.create_line(0, y, width, y, fill="black")

    def demo_grid(self):
        # Set canvas size
        canvas_width = 400
        canvas_height = 400

        # Create a Canvas
        self.canvas = Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.grid(row=0, column=0, sticky=NSEW)

        # Create grid lines
        rows = 10  # Number of rows
        columns = 10  # Number of columns
        self.create_grid(
            self.canvas,
            canvas_width,
            canvas_height,
            rows,
            columns)

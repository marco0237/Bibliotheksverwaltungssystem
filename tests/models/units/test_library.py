# test_library.py
from src.models.book import Book
from src.models.library import Library
from unittest import TestCase
from pathlib import Path
import sys

OUTPUT_PATH = Path(__file__).parents[3]
SRC_PATH = OUTPUT_PATH / Path("./src")
sys.path.append(str(SRC_PATH))


class LibraryTestCase(TestCase):

    def test_create_library(self):
        self.library_1 = Library()  # cree und Objet par rapport à __init__
        self.assertEqual(len(self.library_1.books), 0)
        self.assertEqual(len(self.library_1.members), 0)

    def test_add_book(self):
        library_2 = Library()
        book_1 = Book(
            "Python 3",
            "Johannes Ernesto",
            "987-3-8362-9129-3",
            True)
        library_2.add_book(book_1)
        self.assertEqual(1, len(library_2.books))

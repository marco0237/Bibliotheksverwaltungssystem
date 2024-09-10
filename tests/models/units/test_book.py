

import unittest
from unittest import TestCase

from pathlib import Path
import sys
OUTPUT_PATH = Path(__file__).parents[3]
SRC_PATH = OUTPUT_PATH / Path("./src")
sys.path.append(str(SRC_PATH))


from models.book import Book




# import the package
#import src

# import the antigravity module
#import src.models.book

# or an object inside the antigravity module
#from src.models.book import Book


class BookTestCase(TestCase):

    def test_create_book(self):
        book = Book("Python 3", "Johannes Ernesti", "987-3-8362-9129-3", True)
        self.assertEqual("Johannes Ernesti", book.author)
        self.assertEqual(True, book.available)

    def test_createBook(self):
        book = Book("Python 3", "Johannes Ernesti", "987-3-8362-9129-3", True)
        self.assertEqual("Johannes Ernesti", book.author)
        self.assertEqual(True, book.available)


if __name__ == "__main__":
    unittest.main()

import unittest
from src.library import Library
from src.book import Book
from matplotlib.style import library


class LibraryTestCase(unittest.TestCase):
    def test_add_book(self):
        self.library= Library()
        self.assertEqual(len(self.library.books), 0)  # add assertion here



if __name__ == '__main__':
    unittest.main()

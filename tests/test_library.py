# test_library.py
import unittest
from src.library import Library
from src.book import Book
import sys
print(sys.path)



class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 0)

        book = Book("1984", "George Orwell", "125483", True)
        self.library.add_book(book)

        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "1984")


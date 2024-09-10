from unittest import TestCase
from models.book import Book
 


class BookTestCase(TestCase):

    def test_create_book(self):
        book = Book("Python 3", "Johannes Ernesti", "987-3-8362-9129-3", True)
        self.assertEqual("Johannes Ernesti", book.author)
        self.assertEqual(True, book.available)

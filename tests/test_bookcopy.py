import unittest
from src.book import Book


class BookTestCase222(unittest.TestCase):
    def test_something(self):
        self.book = Book("HARRY POTTER", "James1", "AXBCD_123-GASdk-1223", True)
        self.assertEqual(self.book.author, "James1")  # add assertion here

    def test_something2(self):
        self.book = Book("HARRY POTTER", "James1", "AXBCD_123-GASdk-1223", True)
        self.assertEqual(self.book.author, "James31")  # add assertion here


import unittest
from src.book import Book


class BookTestCase(unittest.TestCase):
    def test_add_book(self):
        self.library= Book()
        self.assertEqual(len(self.library.books), 0)  # add assertion here

if __name__ == '__main__':
    unittest.main()
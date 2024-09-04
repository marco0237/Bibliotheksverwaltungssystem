import unittest
from src.book import Book
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.book = Book("HARRY POTTER", "James1", "AXBCD_123-GASdk-1223", True)
        self.assertEqual(self.book.author, "James1")  # add assertion here


if __name__ == '__main__':
    unittest.main()

import unittest
from src.library import Library
 
# LIB
class LibraryTestCase(unittest.TestCase):
    def test_add_book(self):
        self.library= Library()
        self.assertEqual(len(self.library.books), 0)  # add assertion here



if __name__ == '__main__':
    unittest.main()

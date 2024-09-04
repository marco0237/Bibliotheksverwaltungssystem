import unittest
from book import Book
from src.member import Member


class MemeberTestCase(unittest.TestCase):
    def test_constructor(self):
        list_of_books = [     Book("HARRY POTTER", "James","ABCD_123-GASdk-1223", True) 
]
        self.member =  Member("Ghislain", 1 ,list_of_books)
        self.assertEqual(len(self.library.books), 0)  # add assertion here


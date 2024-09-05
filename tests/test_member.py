
from unittest import TestCase
from src.book import Book
from src.member import Member

class MemberTestCase(TestCase):
   
    def test_create_member(self):
      self.book1 = Book("HARRY POTTER", "James1","AXBCD_123-GASdk-1223", True) 
      self.book2 = Book("Python 4", "James2","1ABCD_123-GASdk-1223", True) 
      self.book3 = Book("FmL machinenbau", "James3","AB1CD_123-GASdk-1223", True) 
    
      self.list_of_books = [self.book1, self.book2,self.book3]
      self.ghislain =  Member("Ghislain", 1 ,self.list_of_books)
      self.assertEqual(self.ghislain.name, "James1")  # add assertion here




  
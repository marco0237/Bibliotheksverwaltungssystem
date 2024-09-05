
from unittest import TestCase
from src.member import Member

class MemberTestCase(TestCase):

    def test_create_member(self):
       self. member = Member("Member 1", 1, [])
       self.assertEqual(1, self.member.id)
    
    # Borrow book
    def test_borrow_book(self):
        pass

    # 
    def test_return_book(self):
        pass
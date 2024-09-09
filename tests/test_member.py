
from unittest import TestCase
from src.member import Member
from src.book import Book


class MemberTestCase(TestCase):

    def test_create_member(self):

        self.member = Member("Member 1", 1)
        self.assertEqual(1, self.member.member_id)
        self.assertEqual(0, len(self.member.borrowed_books))

    # Borrow book

    def test_borrow_book_with3books(self):

        # Setup (ARRANGE)
        self.bookObject = Book("HARRY POTTER", "James",
                               "ABCD_123-GASdk-1223", True)
        self.book1 = Book("HARRY POTTER", "James1",
                          "AXBCD_123-GASdk-1223", True)
        self.book2 = Book("Python 4", "James2", "1ABCD_123-GASdk-1223", True)
        self.book3 = Book("FmL machinenbau", "James3",
                          "AB1CD_123-GASdk-1223", True)
        self.list_of_books = [self.book1, self.book2, self.book3]
        self.member = Member("Ghis", 1)

        # Execution (ACT)
        self.member.borrow_book(self.book3)
        self.member.borrow_book(self.book1)
        self.member.borrow_book(self.book2)

        # Verification (ASSERT)
        self.assertEqual(3, len(self.member.borrowed_books))

        # Borrow book
    def test_borrow_book_notAvailable(self):

        # Setup (ARRANGE)
        self.bookObject = Book("HARRY POTTER", "James",
                               "ABCD_123-GASdk-1223", False)
        self.book1 = Book("HARRY POTTER", "James1",
                          "AXBCD_123-GASdk-1223", True)
        self.book2 = Book("Python 4", "James2", "1ABCD_123-GASdk-1223", True)
        self.book3 = Book("FmL machinenbau", "James3",
                          "AB1CD_123-GASdk-1223", True)
        self.list_of_books = [self.book1, self.book2, self.book3]
        self.member = Member("Ghis", 1)

        # Execution (ACT)
        self.member.borrow_book(self.bookObject)
        self.member.borrow_book(self.book1)
        self.member.borrow_book(self.book2)

        # Verification (ASSERT)
        self.assertEqual(2, len(self.member.borrowed_books))

    #

    def test_return_book_not_exist(self):
        # Setup (ARRANGE)
        self.bookObject = Book("HARRY POTTER", "James",
                               "ABCD_123-GASdk-1223", False)
        self.book1 = Book("HARRY POTTER", "James1",
                          "AXBCD_123-GASdk-1223", True)
        self.book2 = Book("Python 4", "James2", "1ABCD_123-GASdk-1223", True)
        self.book3 = Book("FmL machinenbau", "James3",
                          "AB1CD_123-GASdk-1223", True)
        self.list_of_books = [self.book1, self.book2, self.book3]
        self.member = Member("Ghis", 1)
        self.member.borrow_book(self.book3)
        self.member.borrow_book(self.book1)
        self.member.borrow_book(self.book2)

        # Execution (ACT)
        self.result = self.member.return_book(self.bookObject)

        # Verification (ASSERT)
        self.assertEqual(False, self.result)

    def test_return_book_exist(self):
        # Setup (ARRANGE)
        self.bookObject = Book("HARRY POTTER", "James",
                               "ABCD_123-GASdk-1223", False)
        self.book1 = Book("HARRY POTTER", "James1",
                          "AXBCD_123-GASdk-1223", True)
        self.book2 = Book("Python 4", "James2", "1ABCD_123-GASdk-1223", True)
        self.book3 = Book("FmL machinenbau", "James3",
                          "AB1CD_123-GASdk-1223", True)
        self.list_of_books = [self.book1, self.book2, self.book3]
        self.member = Member("Ghis", 1)
        self.member.borrow_book(self.book3)
        self.member.borrow_book(self.book1)
        self.member.borrow_book(self.book2)

        # Execution (ACT)
        self.result = self.member.return_book(self.book3)

        # Verification (ASSERT)
        self.assertEqual(True, self.result)

from typing import List # Typing concpet in python
from src.book import Book

class Member:    
    
    def __init__(self, name:str, member_id:int) -> None:
         # Attribute:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # empty list

    # Methoden:
    def borrow_book(self, book: Book):
        if book.available:
            self.borrowed_books.append(book)
                      

    def return_book(self, book: Book):
        if  book in self.borrowed_books: # Find  item in list ==: just use if ... in ...
            self.borrowed_books.remove(book)
            return True
        else:
            return False
    

    def __str__(self):
            return f"My name is > {self.name}"
  
            

 
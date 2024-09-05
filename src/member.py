from typing import List # Typing concpet in python
from book import Book

class Member:    
    
    def __init__(self, name:str, member_id:int, borrowed_books: List[Book]) -> None:
         # Attribute:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books  

    # Methoden:
    def borrow_book(self, book: Book):
        if book.available:
            self.borrowed_books.append(book)
                      

    def return_book(self, book: Book):
        if any(book in item for item in self.borrowed_books):
            self.borrowed_books.remove(book)
            return True
        else:
            return False
    

    def __str__(self):
            return f"My name is > {self.name}"
  
            

 
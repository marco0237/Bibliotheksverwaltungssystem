from typing import List # Typing concpet in python
from book import Book


class Member:    
    
    def __init__(self, name:str, id:int, borrowed_books: List[Book]) -> None:
         # Attribute:
        self.name = name
        self.id = id
        self.borrowed_books = borrowed_books  

    # Methoden:
    def borrow_book(self, book: Book) -> str:            
        if book.available:
                  for book_item in  self.borrowed_books:
                     if book_item == book:
                           book_item.available = False
                           return "Ok"
        else:
            return "Book not exists"
                      
                    
                          
                  
           
                  
    
    def return_book(self):
            pass
    

    def __str__(self):
            return f"My name is > {self.name}"
  
            

 
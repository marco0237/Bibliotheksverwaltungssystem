

class Book:
    
    def __init__(self, title:str, author:str, isbn:str, available:bool) -> None:
         # Attribute:
        self.title = title
        self.author = author
        self.isbn = isbn    
        self.available = available

    def  __str__(self):
        return f"This is a book named {self.title} and author = {self.author}"
       
 
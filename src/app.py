from book import Book
from member import Member
from src.library import Library

def main ():
   
    bookObject = Book("HARRY POTTER", "James","ABCD_123-GASdk-1223", True) 

    book1 = Book("HARRY POTTER", "James1","AXBCD_123-GASdk-1223", True) 
    book2 = Book("Python 4", "James2","1ABCD_123-GASdk-1223", True) 
    book3 = Book("FmL machinenbau", "James3","AB1CD_123-GASdk-1223", True) 
    
    list_of_books = [book1, book2,book3]
    ghislain =  Member("Ghislain", 1 ,list_of_books)
    
    #print(bookObject)
    #print(ghislain)
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    print(len(library.books))



    print(ghislain.borrow_book(book2))
    print(ghislain.borrow_book(book2))
    print(ghislain.borrow_book(book1))

# ----------------MAIN-------------------
if "__main__" == __name__:
    main()





















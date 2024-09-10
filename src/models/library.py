from src.models.book import Book
from member import Member
#TDD(test drive developp)

class Library:
    # Initialisierungsmethode Konstruktor
    def __init__(self):
        #self.books = List[Book] # Public Attribut books
        #self.members = List[Member] #Attribut members
        self.books = []  # Public Attribut books
        self.members = list()  # Attribut members

    # Methoden
    def add_book(self, book:Book):
        self.books.append(book)


    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
            #print(f"Buch '{book.title}' wurde entfernt")
        else:
            return False
            #print(f"buch'{book.title}' ist nicht in der Bibiothek")


    def register_member(self, member):
        self.members.append(member)
        return True
        #print(f"Der neuen Miglied heißt'{member.name}'")


    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
            else:
                return False
        #print(f"es existiert kein Buch mit'{isbn}'")

    def list_available_books(self):
        #Auflisten alle verfügbare Bücher
        available_books = []
        for book in self.books:
            if not book.available:
                available_books.append(book)
        if available_books:
            for book in available_books:
                return True
        else:
            return False

    def list_borrowed_books(self):
        # Auflisten alle augeliehen Bücher
        borrowed_books = []
        for book in self.books:
            if book.available:
                borrowed_books.append(book)
        if borrowed_books:
            for book in borrowed_books:
                return True
        else:
            return False
        pass

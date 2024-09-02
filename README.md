# Bibliotheksverwaltungssystem
Anforderungen:
    1. Klasse Book:
        ◦ Attribute:
            ▪ title: Der Titel des Buches.
            ▪ author: Der Autor des Buches.
            ▪ isbn: Die ISBN-Nummer des Buches (eindeutige Kennung).
            ▪ available: Ein Boolean, der angibt, ob das Buch verfügbar ist oder ausgeliehen wurde.
        ◦ Methoden:
            ▪ __str__(): Gibt eine string-basierte Beschreibung des Buches zurück.
    2. Klasse Member:
        ◦ Attribute:
            ▪ name: Der Name des Mitglieds.
            ▪ member_id: Eine eindeutige Mitglieds-ID.
            ▪ borrowed_books: Eine Liste der Bücher, die das Mitglied ausgeliehen hat.
        ◦ Methoden:
            ▪ borrow_book(book): Ermöglicht einem Mitglied, ein Buch auszuleihen, sofern es verfügbar ist.
            ▪ return_book(book): Ermöglicht einem Mitglied, ein Buch zurückzugeben.
            ▪ __str__(): Gibt eine string-basierte Beschreibung des Mitglieds und der ausgeliehenen Bücher zurück.
    3. Klasse Library:
        ◦ Attribute:
            ▪ books: Eine Liste von Büchern, die die Bibliothek besitzt.
            ▪ members: Eine Liste der registrierten Mitglieder.
        ◦ Methoden:
            ▪ add_book(book): Fügt der Bibliothek ein Buch hinzu.
            ▪ remove_book(book): Entfernt ein Buch aus der Bibliothek.
            ▪ register_member(member): Registriert ein neues Mitglied in der Bibliothek.
            ▪ find_book_by_isbn(isbn): Findet ein Buch anhand seiner ISBN-Nummer.
            ▪ list_available_books(): Listet alle verfügbaren Bücher auf.
            ▪ list_borrowed_books(): Listet alle ausgeliehenen Bücher auf.
    4. Erweiterungsmöglichkeiten:
        ◦ Erstelle eine Benutzeroberfläche für das System (kann auch textbasiert sein).
        ◦ Implementiere eine Methode, um Bücher nach Autor oder Titel zu durchsuchen.
        ◦ Füge eine Klasse Librarian hinzu, die administrative Funktionen wie das Hinzufügen oder Entfernen von Büchern ausführt.
        ◦ Implementiere eine Funktion, die die Anzahl der Tage berechnet, die ein Buch ausgeliehen wurde, und möglicherweise eine Gebühr für verspätete Rückgaben berechnet.

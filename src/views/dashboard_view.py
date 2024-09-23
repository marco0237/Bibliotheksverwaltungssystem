import tkinter as tk # Importiere das Tkinter-Modul, um die GUI zu erstellen
# from pathlib import Path
from tkinter import Frame, Label # Importiere spezielle Tkinter-Komponenten
from tkinter.font import Font # Importiere Font, um Schriftarten zu erstellen
# from customtkinter import CTk, CTkCheckBox, CTkButton, CTkFrame, CTkLabel
from controllers.main_controller import MainController
# from shared.constants import ASSETS_PATH
from shared.utils import create_header_label, create_count_label
# from views.frame_base import FrameBase

# Die Hauptklasse für das Dashboard, erbt von Frame
class DashboardView(Frame):
    # Konstruktor: Initialisiert das Dashboard
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)  # Initialisiere das Frame-Objekt
        self.title = "Dashboard"  # Setze den Titel des Dashboards (wird aber nicht direkt verwendet)
        self.controller = controller  # Speichere den Controller (für spätere Datenaufrufe)

        # Konfiguration der Spalten (Grid): Definiere die Gewichtung für Spalten (damit sich die GUI gut anpasst)
        self.grid_columnconfigure(0, weight=0)  # Spalte 0: feste Breite
        self.grid_columnconfigure(1, weight=0)  # Spalte 1: feste Breite
        self.grid_columnconfigure(2, weight=0)  # Spalte 2: feste Breite
        self.grid_columnconfigure(3, weight=1)  # Spalte 3: kann sich flexibel anpassen

        # Konfiguration der Zeilen: Definiere die Gewichtung für die Zeilen
        self.grid_rowconfigure(0, weight=0)  # Zeile 0: feste Höhe
        self.grid_rowconfigure(1, weight=0)  # Zeile 1: feste Höhe
        self.grid_rowconfigure(2, weight=1)  # Zeile 2: kann sich flexibel anpassen

        # Definiere Schriftarten für die Labels
        self.stringFont = Font(family="Helvetica", size=60, weight="bold")  # Große Schrift für Header
        self.numberFont = Font(family="Montserrat Bold", size=36, weight="bold")  # Kleinere Schrift für Zahlen

        self.__initUI__()  # Rufe die Methode auf, um die Benutzeroberfläche (UI) zu initialisieren

        self.update_ui()  # Initialisiere die Anzeige der aktuellen Werte

    # Methode zum Initialisieren der Benutzeroberfläche
    def __initUI__(self):
        # "Borrowed"-Sektion
        borrowed_frame = Frame(self, padx=1, pady=1)  # Erstelle ein Frame für "Borrowed"
        borrowed_frame.grid(row=0, column=0)  # Platziere das Frame in Zeile 0, Spalte 0
        borrowed_label = create_header_label(borrowed_frame, "Borrowed:", self.stringFont)  # Erstelle das Header-Label
        borrowed_label.grid(row=1, column=0)  # Platziere das Header-Label im Frame
        self.borrowedValueLabel = create_count_label(borrowed_frame, " 350", self.numberFont)  # Erstelle das Zahlen-Label
        self.borrowedValueLabel.grid(row=1, column=1)  # Platziere das Zahlen-Label im Frame

        # "Members"-Sektion
        members_frame = Frame(self, padx=1, pady=1)  # Erstelle ein Frame für "Members"
        members_frame.grid(row=0, column=3)  # Platziere es in Zeile 0, Spalte 1
        member_label = create_header_label(members_frame, "Members:", self.stringFont)  # Erstelle das Header-Label
        member_label.grid(row=0, column=3)  # Platziere das Header-Label im Frame
        self.membersValueLabel = create_count_label(members_frame, "4.1k", self.numberFont)  # Erstelle das Zahlen-Label
        self.membersValueLabel.grid(row=0, column=5)  # Platziere das Zahlen-Label im Frame

        # "Available Books"-Sektion
        available_books_frame = Frame(self, padx=1, pady=1)  # Erstelle ein Frame für "Avail.Books"
        available_books_frame.grid(row=3, column=0)  # Platziere es in Zeile 1, Spalte 0
        available_books_label = create_header_label(available_books_frame, "Avail.Books:", self.stringFont)  # Header-Label
        available_books_label.grid(row=3, column=0)  # Platziere das Header-Label im Frame
        self.availableBooksValueLabel = create_count_label(available_books_frame, " 311b", self.numberFont)  # Zahlen-Label
        self.availableBooksValueLabel.grid(row=3, column=1)  # Platziere das Zahlen-Label im Frame

    # Methode zum Aktualisieren der UI mit aktuellen Daten (z.B. aus dem Controller)
    def update_ui(self):
        print(f"===================== {type(self.controller)}")  # Debug-Ausgabe des Controllers
        # Aktualisiere das Label für die Mitgliederanzahl basierend auf den Daten vom Controller
        self.membersValueLabel.configure(text=len(self.controller.load_members()))  # Anzahl der Mitglieder

# Hilfsfunktion zum Erstellen eines Header-Labels
def create_header_label(parent, text, font):
    label = Label(parent, text=text, font=font)  # Erstelle ein Label mit Text und Schriftart
    return label  # Gib das Label zurück

# Hilfsfunktion zum Erstellen eines Zahlen-Labels
def create_count_label(parent, text, font):
    label = Label(parent, text=text, font=font)  # Erstelle ein Label mit Zahlenwert und Schriftart
    return label  # Gib das Label zurück

# Main-Block: Startet die GUI
if __name__ == "__main__":
    root = tk.Tk()  # Erstelle das Hauptfenster
    root.title("Dashboard")  # Setze den Fenstertitel
    controller = MainController()  # Erstelle eine Instanz des Controllers
    app = DashboardView(root, controller)  # Erstelle die Dashboard-View und übergebe das Hauptfenster und den Controller
    app.pack(fill="both", expand=True)  # Packe die View ins Fenster und lasse es sich anpassen
    root.mainloop()  # Starte die Tkinter-Hauptschleife (zeigt das Fenster und hält es offen)

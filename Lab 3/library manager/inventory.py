import json
import logging
from pathlib import Path
from .book import Book

logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

CATALOG_FILE = Path("catalog.json")


class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        logging.info(f"Added book: {book.title}")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return "\n".join(str(book) for book in self.books)

    def save_books(self):
        try:
            with open(CATALOG_FILE, "w") as file:
                json.dump([b.to_dict() for b in self.books], file, indent=4)
        except Exception as e:
            logging.error(f"Error saving file: {e}")

    def load_books(self):
        try:
            if not CATALOG_FILE.exists():
                self.save_books()
                return
            with open(CATALOG_FILE, "r") as file:
                data = json.load(file)
                self.books = [Book(**b) for b in data]
        except Exception as e:
            logging.error(f"Error loading file: {e}")
            self.books = []
            self.save_books()

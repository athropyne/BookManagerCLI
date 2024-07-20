from exc import BookNotFound
from services.library.models import Status
from core.storage import Storage


class Repository:
    """Класс для работы с данными"""
    def __init__(self, storage: Storage):
        self.storage = storage

    def add(self, book: dict):
        books = self.storage.get()
        books.append(book)
        self.storage.save(books)

    def remove(self, book_id: str):
        books = self.storage.get()
        exists_flag: bool = False
        for book in books:
            if book["ID"] == book_id:
                books.remove(book)
                exists_flag = True
                break
        if not exists_flag:
            raise BookNotFound
        self.storage.save(books)

    def find(self, search_term: str) -> list[dict]:
        books = self.storage.get()

        found_books = [book
                       for book in books
                       if search_term.lower() in book["title"].lower()
                       or search_term.lower() in book["author"].lower()
                       or search_term.lower() in book["year"].lower()]
        return found_books

    def list(self) -> list[dict]:
        return self.storage.get()

    def update(self, book_id: str, status: Status):
        books = self.storage.get()
        exists_flag: bool = False
        for book in books:
            if book["ID"] == book_id:
                book["status"] = status
                exists_flag = True
                break
        if not exists_flag:
            raise BookNotFound
        self.storage.save(books)

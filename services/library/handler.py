import dataclasses
import uuid

import exc
from exc import BookNotFound
from services.library.models import Book, Status
from services.library.repository import Repository


class Handler:
    """обработчик команд. Публичные методы класса подготавливают данные для записи в базу данных
    и используют объект класса Repository для взаимодействия с базой"""

    def __init__(self, repository: Repository):
        self.repository = repository

    def __list_result_print(self, result: list):
        for i in result:
            for k, v in i.items():
                print(k, "\t", "\t", v)
            print()

    def add(self, title, author, year):
        book = Book(
            ID=str(uuid.uuid4()),
            title=title,
            author=author,
            year=year,
            status=Status.in_stock
        )
        self.repository.add(dataclasses.asdict(book))
        print("Книга добавлена")

    def remove(self, book_id: str):
        self.repository.remove(book_id)
        print("Книга удалена")

    def find(self, search_term: str):
        books: list[dict] = self.repository.find(search_term)
        print("Найденные книги:") if len(books) else print("книги не найдены")
        self.__list_result_print(books)

    def list(self):
        books = self.repository.list()
        print("Список всех книг:") if len(books) else print("книги не найдены")
        self.__list_result_print(books)

    def update(self, book_id: str, status: Status):
        if status not in list(Status):
            raise exc.InvalidData(
                f"""Поле `status` с некорректным значением. Допускается только `{Status.issued}` и `{Status.in_stock}`""")
        try:
            self.repository.update(book_id, status)
            print("Статус книги обновлен")
        except BookNotFound as e:
            print(e.msg)

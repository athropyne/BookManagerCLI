from argparse import ArgumentParser

from core.parser import BaseParser
from services.library.module import adapter


class Chapter(BaseParser):
    """класс представляет раздел с командами. Раздел именуется параметром `command_name`.
    Имя раздела является префиксом для набора команд.
    Свойство `command_mapping` представляет собой словарь,
    где ключами - имена команд, а значениями - ссылки на методы адаптера.

    Примеры команд представляющих этот раздел:

    python main.py <command_name> --add Керри "Стивен Кинг" 1974

    python main.py <command_name> --find 1974

    python main.py <command_name> --list"""
    def __init__(self, command_name: str, subparsers):
        super().__init__(command_name, subparsers)
        self.parser: ArgumentParser = subparsers.add_parser(command_name, help="Команды для работы с книгами")
        self.parser.add_argument("--add", nargs=3, metavar=("TITLE", "AUTHOR", "YEAR"), help="Добавить новую книгу")
        self.parser.add_argument("--remove", metavar="ID", help="Удалить книгу по ID")
        self.parser.add_argument("--find", metavar="SEARCH_TERM", help="Найти книги по названию, автору или году")
        self.parser.add_argument("--list", action="store_true", help="Отобразить все книги")
        self.parser.add_argument("--update", nargs=2, metavar=("ID", "STATUS"), help="Обновить статус книги")
        self.command_mapping = dict(
            add=adapter.add,
            remove=adapter.remove,
            find=adapter.find,
            list=adapter.list,
            update=adapter.update
        )


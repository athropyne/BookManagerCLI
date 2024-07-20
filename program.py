import argparse
from typing import TypeVar, Generic, Type

from core.parser import BaseParser

T = TypeVar('T', bound=BaseParser)


class Program(Generic[T]):
    "Основной класс программы. Аккумулирует в себе парсеры и запускает прослушивание команд с консоли"

    def __init__(self, **parsers: Type[T]):
        """Принимает неограниченное число параметров. Параметры - ссылки на классы производные от BaseParser
        `command_mapping` - словарь с ключами разделов, значениями которого является свойство `command_mapping`
        екземпляра класса, производного от BaseParser
        """
        self.main_parser = argparse.ArgumentParser(description="Управление библиотекой книг")
        self.subparsers = self.main_parser.add_subparsers(dest="command")
        self.command_mapping = {}
        for k, v in parsers.items():
            self.command_mapping[k] = v(k, self.subparsers).command_mapping

    def run(self):
        """запускает анализ комманд.
        сначала вычленяет имя раздела `chapter`,
        затем в цикле проходит по словарю свойст объекта `args`.
        если значение свойства определено - значит это и есть введенная команда.
        команда вызывается из словаря `self.command_mapping` с двумя ключами, которые хранят ссылку на методы объекта `Adapter`.
        Первый ключ - раздел , второй ключ - команда, значение - полученные аргументы из командной строки.
        """
        args: argparse.Namespace = self.main_parser.parse_args()
        mapping = args.__dict__
        chapter = mapping["command"]
        del mapping["command"]

        for k, v in args.__dict__.items():
            if v:
                self.command_mapping[chapter][k](v)
                break
        # return args

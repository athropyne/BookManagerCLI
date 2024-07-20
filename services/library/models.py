from dataclasses import dataclass
from enum import Enum

"""Модуль с классами данных"""


class Status(str, Enum):
    issued = "выдана"
    in_stock = "в наличии"


@dataclass
class Book:
    """объектное представление книги. поля класса представляют поля книги"""
    ID: str
    title: str
    author: str
    year: int
    status: Status



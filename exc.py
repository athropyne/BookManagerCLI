"""ошибки"""

class BookNotFound(Exception):
    def __init__(self):
        self.msg = "Книга не найдена"


class NoResult(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class InvalidData(Exception):
    def __init__(self, msg: str):
        self.msg = msg

from services.library.handler import Handler


class Adapter:
    """Методы класса служат связкой между сырыми аргументами команд и API обработчиков (Handler)"""

    def __init__(self, handler: Handler):
        self.handler = handler

    def add(self, data: list):
        self.handler.add(*data)

    def remove(self, ID: str):
        self.handler.remove(ID)

    def find(self, search_term: str):
        self.handler.find(search_term)

    def list(self, _: bool):
        self.handler.list()

    def update(self, data: list):
        self.handler.update(*data)

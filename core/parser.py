from abc import ABC, abstractmethod


class BaseParser(ABC):
    """интерфейс представляющий отдельные парсеры"""
    @abstractmethod
    def __init__(self, command_name: str, parser):
        self.parser = parser
        self.command_name = command_name
        self.command_mapping = {}

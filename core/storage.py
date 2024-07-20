import json


class Storage:
    """база данных (json файл)"""
    def __init__(self, db_name: str):
        self.db_name = db_name

    def get(self):
        """получает все данные из json файла"""
        try:
            with open(self.db_name, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            print("данные повреждены")

    def save(self, books: list):
        """сохраняет json файл"""
        with open(self.db_name, "w") as file:
            json.dump(books, file, indent=4)


storage = Storage("library.json")
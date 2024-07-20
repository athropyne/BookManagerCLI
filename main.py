"""главный файл программы"""

from program import Program
from services.library.chapter import Chapter


if __name__ == "__main__":
    program = Program(book=Chapter)
    args = program.run()

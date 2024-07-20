from core.storage import storage
from services.library.adapter import Adapter
from services.library.handler import Handler
from services.library.repository import Repository

"""Инициализация зависимостей"""
repository = Repository(storage)
handler = Handler(repository)
adapter = Adapter(handler)

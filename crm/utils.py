"""
Вспомогательные функции для работы с ID.

Функции:
- get_next_id() — возвращает следующий доступный ID для нового клиента/услуги.

Зависимости:
- Нет внешних зависимостей.

Источник:
- Код написан с нуля для этого проекта.
"""


import os


def clear_screen():
    """Очищает экран терминала."""
    os.system("cls" if os.name == "nt" else "clear")


def get_next_id(items):
    """Возвращает следующий доступный ID."""
    return max((int(item["id"]) for item in items), default=0) + 1

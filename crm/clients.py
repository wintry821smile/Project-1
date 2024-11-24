"""
Модуль для работы с клиентами.

Функции:
- find_or_create_client() — находит клиента по имени или ID, либо создает нового.
- list_all_clients() — выводит список всех клиентов.
- update_client_info() — обновляет информацию о клиенте.
- _load_clients() — загружает список клиентов из CSV.
- _save_clients() — сохраняет список клиентов в CSV.

Зависимости:
- csv — для работы с CSV файлами.
- os — для работы с файловой системой.
- datetime — для работы с датами и временем (вспомогательные функции для обработки и сортировки данных).
- utils.py — вспомогательные функции для работы с ID клиентов.

Источник:
- ChatGPT участвовал в рефакторинге кода
"""


import csv
import os
from utils import get_next_id

# Путь к файлу клиентов относительно директории main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENTS_FILE = os.path.join(BASE_DIR, "data", "clients.csv")

def find_or_create_client():
    """Находит клиента по имени или ID, либо создает нового."""
    clients = _load_clients()
    identifier = input("Введите имя или ID клиента: ").strip()

    for client in clients:
        if identifier in (client["name"], client["id"]):
            print("Клиент найден.")
            return client

    print("Клиент не найден. Создаем нового.")
    return _create_new_client(clients)


def list_all_clients():
    """Выводит список всех клиентов."""
    clients = _load_clients()
    print("\n=== Список всех клиентов ===")
    for client in clients:
        print(f"{client['id']} - {client['name']} ({client['info']})")
    input("\nНажмите Enter, чтобы вернуться.")


def update_client_info(client):
    """Обновляет информацию о клиенте."""
    print("\n=== Обновление данных клиента ===")
    client["name"] = input("Введите новое имя: ").strip()
    client["info"] = input("Введите дополнительную информацию: ").strip()
    _save_clients([client])


def _create_new_client(clients):
    """Создает нового клиента."""
    new_client = {
        "id": str(get_next_id(clients)),
        "name": input("Введите имя клиента: ").strip(),
        "info": input("Введите дополнительную информацию о клиенте: ").strip(),
        "service_count": "0",
    }
    clients.append(new_client)
    _save_clients(clients)
    return new_client


def _load_clients():
    """Загружает список клиентов из CSV."""
    try:
        with open(CLIENTS_FILE, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def _save_clients(clients):
    """Сохраняет список клиентов в CSV."""
    os.makedirs(os.path.dirname(CLIENTS_FILE), exist_ok=True)  # Создать папку, если её нет
    with open(CLIENTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "info", "service_count"])
        writer.writeheader()
        writer.writerows(clients)

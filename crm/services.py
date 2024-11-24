"""
Модуль для работы с услугами/товарами клиентов.

Функции:
- add_service() — добавляет услугу или товар для клиента.
- list_services() — выводит список услуг/товаров, предоставленных клиенту.
- _load_services() — загружает список услуг из CSV.
- _save_services() — сохраняет список услуг в CSV.

Зависимости:
- csv — для работы с CSV файлами.
- os — для работы с файловой системой.
- datetime — для работы с датами и временем.
- utils.py — вспомогательные функции для работы с ID услуг.

Источник:
- ChatGPT участвовал в рефакторинге кода
"""


import csv
import os
from datetime import datetime
from utils import get_next_id

# Путь к файлу услуг относительно директории main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICES_FILE = os.path.join(BASE_DIR, "data", "services.csv")


def add_service(client_id):
    """Добавляет услугу или товар для клиента."""
    while True:
        try:
            deadline = input("Введите дедлайн (ДД-ММ-ГГГГ): ").strip()
            # Проверяем корректность формата даты
            deadline_date = datetime.strptime(deadline, "%d-%m-%Y")
            break
        except ValueError:
            print("Ошибка: неверный формат даты. Попробуйте снова.")

    service = {
        "id": str(get_next_id(_load_services())),
        "client_id": client_id,
        "name": input("Введите название услуги/товара: ").strip(),
        "price": input("Введите цену: ").strip(),
        "deadline": deadline_date.strftime("%d-%m-%Y"),
        "info": input("Введите дополнительную информацию: ").strip(),
        "date": datetime.now().strftime("%d-%m-%Y"),
    }
    services = _load_services()
    services.append(service)
    _save_services(services)
    print("Услуга/товар успешно добавлена.")


def list_services(client_id):
    """Выводит список услуг/товаров клиента."""
    services = [s for s in _load_services() if s["client_id"] == client_id]
    services.sort(key=lambda x: datetime.strptime(x["date"], "%d-%m-%Y"))
    print("\n=== Услуги/товары клиента ===")
    for idx, service in enumerate(services, start=1):
        print(f"{idx}. {service['name']} - {service['price']} (Дедлайн: {service['deadline']})")
        print(f"    Дополнительная информация: {service['info']}")
    input("\nНажмите Enter, чтобы вернуться.")


def _load_services():
    """Загружает список услуг из CSV."""
    try:
        with open(SERVICES_FILE, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def _save_services(services):
    """Сохраняет список услуг в CSV."""
    os.makedirs(os.path.dirname(SERVICES_FILE), exist_ok=True)  # Создать папку, если её нет
    with open(SERVICES_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["id", "client_id", "name", "price", "deadline", "info", "date"]
        )
        writer.writeheader()
        writer.writerows(services)

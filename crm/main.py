from clients import find_or_create_client, list_all_clients, update_client_info
from services import add_service, list_services
from utils import clear_screen


def main():
    while True:
        clear_screen()
        print("=== Terminal CRM ===")
        print("0 - Показать всех клиентов")
        print("1 - Найти или создать клиента")
        print("2 - Выйти")
        choice = input("Выберите действие: ")

        if choice == "0":
            list_all_clients()
        elif choice == "1":
            client = find_or_create_client()
            client_menu(client)
        elif choice == "2":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


def client_menu(client):
    """Меню клиента."""
    while True:
        clear_screen()
        print(f"=== Клиент: {client['name']} ===")
        print("1 - Добавить услугу/товар")
        print("2 - Показать список услуг/товаров")
        print("3 - Изменить данные клиента")
        print("4 - Вернуться в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_service(client["id"])
        elif choice == "2":
            list_services(client["id"])
        elif choice == "3":
            update_client_info(client)
        elif choice == "4":
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
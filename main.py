import re
from typing import Any

from src.generators import filter_by_currency
from src.pandas_work import read_file
from src.processing import dictionary_filter, filter_by_regex, sort_by_date
from src.utils import read_json, transaction_operation
from src.widget import date_output, masks_card_and_account


def get_status() -> str:
    """Получаем статус от пользователя"""
    print(
        "Введите статус по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    user_input = input().upper()
    if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
        return user_input
    else:
        print(f'Статус операции "{user_input}" недоступен.')
        get_status()
    return user_input


def sorted_date(data: list) -> list:
    user_input = input("Отсортировать операции по дате? Да/Нет\n").lower()
    match user_input:
        case "да":
            is_correct = False
            reverse = False
            while not is_correct:
                user_input = input("Отсортировать по возрастанию или по убыванию?\n").lower()
                if user_input == "по возрастанию":
                    reverse = True
                    is_correct = True
                elif user_input == "по убыванию":
                    reverse = False
                    is_correct = True
            data = sort_by_date(data, reverse)
        case "нет":
            return data
        case _:
            sorted_date(data)
    return data


def currency_rub(data: list) -> list:
    user_input = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
    match user_input:
        case "да":
            new_data = [i for i in filter_by_currency(data, "RUB")]
            return new_data
        case "нет":
            return data
        case _:
            currency_rub(data)
    return data


def search_regex(data: list) -> list:

    user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    match user_input:
        case "да":
            new_data = [i for i in filter_by_regex(data, input("Введите тест: ").lower())]
            return new_data
        case "нет":
            return data
        case _:
            search_regex(data)
    return data


def selection(data: list) -> list:
    status = get_status()
    data = dictionary_filter(data, status)
    data = sorted_date(data)
    data = currency_rub(data)
    data = search_regex(data)
    return data


def start() -> list:
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакициями."
        "\nВыберите необходимый пункт меню:"
        "\n1. Получить информацию о транзакциях из json файла"
        "\n2. Получить информацию о транзакциях из csv файла"
        "\n3. Получить информацию о транзакциях из xlsx файла"
    )
    data = []
    match input():
        case "1":
            print("Для обработки выбран json файл.")
            json_file = read_json("data/operations.json")
            data = selection(json_file)
        case "2":
            print("Для обработки выбран csv файл.")
            csv_file = read_file("data/transactions.csv")
            data = selection(csv_file)
        case "3":
            print("Для обработки выбран xlsx файл.")
            xlsx_file = read_file("data/transactions_excel.xlsx")
            data = selection(xlsx_file)
        case _:
            print("Нет такого варианта. Попробуйте еще раз.")
            start()
    return data


def main() -> Any:
    data = start()

    print("Распечатываю итоговый список транзакций...")

    if data and len(data) != 0:
        print(f"Всего банковских операций в выборке: {len(data)}\n\n")
        for transaction in data:
            print(date_output(transaction["date"]), transaction.get("description"))
            if re.search("Перевод", transaction["description"]):
                print(
                    masks_card_and_account(transaction["from"]), "->", masks_card_and_account(transaction["to"]), "\n"
                )
            else:
                print(masks_card_and_account(transaction["to"]))
                print(f"Сумма: {transaction_operation(transaction)} руб.\n")
    else:
        print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()

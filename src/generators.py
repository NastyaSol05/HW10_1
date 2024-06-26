from typing import Iterator


def filter_by_currency(transactions: list[dict], key: str) -> Iterator:
    """Функция, которая возвращает итераторы по очереди операции, в которых указана заданная валюта"""
    if "operationAmount" in transactions[0]:
        for trans in transactions:
            if "operationAmount" in trans and trans["operationAmount"]["currency"]["code"] == key:
                yield trans
    else:
        for trans in transactions:
            if trans["currency_code"] == key:
                yield trans


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """Функция, которая возвращает итератор по описаниям транзакций"""
    for trans in transactions:
        yield trans["description"]


def card_number_generator(start: int, end: int) -> Iterator:
    """Функция, которая генерирует номера карт в формате XXXX XXXX XXXX XXXX, где Х - цифра"""
    for i in range(start, end + 1):
        lst = str(i).zfill(16)
        yield f"{lst[:4]} {lst[4:8]} {lst[8:12]} {lst[12:]}"

import datetime
import re
from collections import Counter

from src.widget import date_output


def dictionary_filter(list_dict: list, state: str = "EXECUTED") -> list:
    """
    Функция, которая возвращает новый список,  содержащий только,
    у которых ключ stage содержит переданное в функцию значение
    """
    new_list_dict = []
    for i in list_dict:
        if i.get("state") == state:
            new_list_dict.append(i)
    return new_list_dict


def sort_by_date(list_dict: list, reverse: bool = False) -> list:
    """Функция сортирует список со словарями по дате, поубыванию или возрастанию"""
    if not reverse:
        return sorted(
            list_dict, key=lambda x: datetime.datetime.strptime(date_output(x["date"]), "%d.%m.%Y"), reverse=True
        )
    else:
        return sorted(list_dict, key=lambda x: datetime.datetime.strptime(date_output(x["date"]), "%d.%m.%Y"))


def filter_by_regex(data: list, regex: str) -> list:
    """ функция принимает список с банковскими операциях и строку поиска и возвращает список, где есть данная строка"""
    list_regex = []
    pattern = re.compile(rf"\b{regex.lower()}\b")
    for i in data:
        if "description" in i and re.search(pattern, i.get("description").lower()):
            list_regex.append(i)
    return list_regex


def operation_categories(operations: list, categories: dict) -> dict:
    """ функция, которая возвращает словарь, в котором ключи — названия категорий, значения — количество операций """
    categories_counter: dict[str, int] = Counter()
    for i in operations:
        if 'description' in i:
            for category, key in categories.items():
                if any(j.lower() in i.get("description").lower() for j in key):
                    categories_counter[category] += 1
                    break

    return categories_counter

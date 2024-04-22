import datetime

from src.widget import date_output


def dictionary_filter(list_dict: list, state: str = "EXECUTED") -> list:
    """
    Функция, которая возвращает новый список,  содержащий только,
    у которых ключ stage содержит переданное в функцию значение
    """
    new_list_dict = []
    for i in list_dict:
        if i["state"] == state:
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

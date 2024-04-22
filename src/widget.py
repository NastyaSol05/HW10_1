from src.masks import number_account, number_card


def masks_card_and_account(card_or_account: str) -> str:
    """Функцию, которая работает как с картами, так и со счетами и возвращает их маску"""
    number = card_or_account.split(" ")[-1]

    if "Счет" in card_or_account:
        return f"Счет {number_account(number)}"
    else:
        return f"{card_or_account.replace(number, "")}{number_card(number)}"


def date_output(datetimes: str) -> str:
    """Функция, которая возвращает строку с датой"""
    return f'{datetimes[8:10]}.{datetimes[5:7]}.{datetimes[:4]}'

def masks_card_and_account(card_or_account: str) -> str:

    """ Функцию, которая работает как с картами, так и со счетами и возвращает их маску"""

    if card_or_account[:12] == "Visa Classic":
        return f'{card_or_account[:17]} {card_or_account[17:19]}** **** {card_or_account[25:]}'

    elif card_or_account[:9] == "Visa Gold":
        return f'{card_or_account[:14]} {card_or_account[14:16]}** **** {card_or_account[22:]}'

    elif card_or_account[:13] == "Visa Platinum":
        return f'{card_or_account[:18]} {card_or_account[18:20]}** **** {card_or_account[26:]}'

    elif card_or_account[:7] == "Maestro":
        return f"{card_or_account[:13]} {card_or_account[12:14]}** **** {card_or_account[20:]}"

    else:
        return f"{card_or_account[:4]} **{card_or_account[21:]}"





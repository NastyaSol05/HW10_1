def number_card(card): return f"{card[:4]} {card[4:6]}** **** {card[12:]}"


def number_account(number): return f"**{number[16:]}"


print(number_account('73654108430135874305'))


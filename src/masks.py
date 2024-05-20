from src.logger import logger


def number_card(card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("get correct number card")
    return f"{card[:4]} {card[4:6]}** **** {card[12:]}"


def number_account(number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info("get correct number account")
    return f"**{number[16:]}"

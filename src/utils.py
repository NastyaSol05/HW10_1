import json
import os
from typing import Any

import requests  # type: ignore
from dotenv import load_dotenv

from src.logger import logger

load_dotenv()
API_KEY = os.getenv("API_KEY")


def read_json(path: str) -> Any:
    """Функция, которая  принимает на вход путь до JSON-файла и возвращает список"""
    try:
        file = open(os.path.abspath(path), encoding="utf-8")
        logger.info("open json file")
    except IOError:
        logger.error("can't open json file")
        return []
    else:
        with file:
            logger.info("read json file")
            return json.load(file)


def transaction_operation(operation: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    if "operationAmount" in operation:
        value = operation["operationAmount"]["currency"]["code"]
    else:
        value = operation.get("currency_code")

    logger.info(f"get {value} operation amount")
    if value == "RUB":
        return float(operation["operationAmount"]["amount"])
    elif value in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={value}&amount=1"

        payload: dict = {}
        headers: dict = {"apikey": API_KEY}

        response = requests.get(url, headers=headers, data=payload)

        if response.ok:
            logger.info("response received")
            result = response.json()

            if "operationAmount" in operation:
                amount = operation["operationAmount"]["amount"]
            else:
                amount = operation.get("amount")

            return float(result["result"] * float(amount))

        return 0.0
    else:
        logger.error("can't get operation amount")
        return 0.0

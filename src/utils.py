import json
import os
from typing import Any

import requests  # type: ignore
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def read_json(path: str) -> Any:
    """Функция, которая  принимает на вход путь до JSON-файла и возвращает список"""
    try:
        file = open(os.path.abspath(path), encoding="utf-8")
    except IOError:
        return []
    else:
        with file:
            return json.load(file)


def transaction_operation(operation: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    value = operation["operationAmount"]["currency"]["code"]
    if value == "RUB":
        return float(operation["operationAmount"]["amount"])
    elif value in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={value}&amount=1"

        payload: dict = {}
        headers: dict = {"apikey": API_KEY}

        response = requests.get(url, headers=headers, data=payload)

        result = response.json()
        amount = operation["operationAmount"]["amount"]
        return float((result["result"] + float(amount)) * result["result"] / float(amount))
    else:
        return 0.0


print(
    transaction_operation(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
)

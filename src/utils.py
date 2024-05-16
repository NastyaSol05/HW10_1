import json
import os
from typing import Any

import requests  # type: ignore
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def loads_json(path: str) -> Any:
    """Функция, которая  принимает на вход путь до JSON-файла и возвращает список"""
    with open(os.path.abspath(path), encoding="utf-8") as f:
        if os.stat(path).st_size == 0:
            return []
        else:
            return json.load(f)


def operation_returns(operation: dict) -> str:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    value = operation["operationAmount"]["currency"]["code"]
    if value == "RUB":
        return str(operation["operationAmount"]["amount"])
    elif value in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={value}&amount=1"

        payload: dict = {}
        headers: dict = {"apikey": API_KEY}

        response = requests.get(url, headers=headers, data=payload)

        result = response.json()
        amount = operation["operationAmount"]["amount"]
        return str(result["result"] * float(amount))
    else:
        return "0.0"

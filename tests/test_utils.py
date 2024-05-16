import json
import unittest
from unittest.mock import patch

from src.utils import loads_json, operation_returns


def test_loads_json() -> None:
    """Тест функции loads_json"""

    mock_json_data = {"ключ1": "поддельное значение1", "ключ2": "поддельное значение2"}

    mock_open = unittest.mock.mock_open(read_data=json.dumps(mock_json_data))

    with unittest.mock.patch("builtins.open", mock_open), unittest.mock.patch("os.stat") as mock_stat:
        mock_stat.return_value.st_size = 2

        data = loads_json("data.json")

    assert data == mock_json_data


@patch("requests.get")
def test_operation_returns(mock_get: None) -> None:
    """Тест функции operation_returns"""
    response_value = "90297.21"

    operation = operation_returns(
        {
            "id": 893507143,
            "state": "EXECUTED",
            "date": "2018-02-03T07:16:28.366141",
            "operationAmount": {"amount": "90297.21", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 37653295304860108767",
        }
    )

    assert operation == response_value

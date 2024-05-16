from unittest.mock import patch

from src.utils import loads_json, operation_returns


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

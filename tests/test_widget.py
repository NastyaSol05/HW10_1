import pytest

from src.widget import date_output, masks_card_and_account


@pytest.mark.parametrize(
    "card_or_account, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_masks_card_and_account(card_or_account: str, expected_result: str) -> None:
    assert masks_card_and_account(card_or_account) == expected_result


@pytest.mark.parametrize(
    "datetimes, expected_result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_date_output(datetimes: str, expected_result: str) -> None:
    assert date_output(datetimes) == expected_result

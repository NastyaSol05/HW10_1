import pytest
from src.masks import number_card, number_account


@pytest.fixture
def my_card():
    return "7000792289606361"


def test_number_card(my_card):
    assert number_card(my_card) == "7000 79** **** 6361"


@pytest.fixture
def my_account():
    return '73654108430135874305'


def test_number_account(my_account):
    assert number_account(my_account) == '**4305'

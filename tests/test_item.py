"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def item3():
    return Item("Холодильник", 30000, 10)


def test__init__(item3):

    assert item3.name == "Холодильник"
    assert item3.price == 30000


def test_calculate_total_price(item3):
    assert Item.calculate_total_price(item3) == 300000


def test_apply_discount(item3):
    Item.pay_rate = 0.5
    assert Item.apply_discount(item3) == 15000
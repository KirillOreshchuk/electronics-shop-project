"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def item3():
    return Item("Холодильник", 30000, 10)


@pytest.fixture()
def item4():
    return Item("Микроволновка", 10000, 15)


def test__init__(item3):
    assert item3.name == "Холодильник"
    assert item3.price == 30000


def test_calculate_total_price(item3):
    assert Item.calculate_total_price(item3) == 300000


def test_apply_discount(item3):
    Item.pay_rate = 0.5
    assert Item.apply_discount(item3) == 15000


def test_name(item3):
    assert item3.name == "Холодильник"
    item3.name = "Будильник"
    assert item3.name == "Будильник"


def test_repr(item3):
    assert repr(item3) == "Item('Холодильник', 30000, 10)"


def test_str(item3):
    assert str(item3) == "Холодильник"


def test__add__(item3, item4):
    assert item3 + item4 == 25


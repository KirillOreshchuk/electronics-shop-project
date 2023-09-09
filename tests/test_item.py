"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


item3 = Item("Холодильник", 30000, 10)


def test_item_init():

    assert item3.name == "Холодильник"
    assert item3.price == 30000


def test_calculate_total_price():
    assert item3.calculate_total_price() == 300000


def test_apply_discount():
    Item.pay_rate = 0.5
    assert item3.apply_discount() == 15000
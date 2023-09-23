import pytest


from src.item import Item
from src.phone import Phone


@pytest.fixture()
def item3():
    return Item("Холодильник", 30000, 10)


@pytest.fixture()
def item4():
    return Item("Микроволновка", 10000, 15)


@pytest.fixture()
def phone2():
    return Phone("Samsung", 100000, 9, 2)


@pytest.fixture()
def phone3():
    return Phone("Motorolla", 15000, 16, 1)


def test__init__(phone2):
    assert phone2.name == "Samsung"
    assert phone2.price == 100000
    assert phone2.quantity == 9
    assert phone2.number_of_sim == 2


def test_repr(phone2):
    assert repr(phone2) == "Phone('Samsung', 100000, 9, 2)"


def test_str(phone2):
    assert str(phone2) == "Samsung"


def test__add__(item3, phone3):
    assert item3 + phone3 == 26


def test_number_of_sim(phone2):
    assert phone2.number_of_sim == 2
    phone2.number_of_sim = 1
    assert phone2.number_of_sim == 1


import pytest

from src.keyboard import Keyboard


@pytest.fixture
def kb1():
    return Keyboard("Keyboard1", 1400, 20)


def test__init__(kb1):
    assert kb1.name == "Keyboard1"
    assert kb1.price == 1400
    assert kb1.quantity == 20


def test_change_lang(kb1):
    assert kb1.language == "EN"
    kb1.change_lang()
    assert kb1.language == "RU"
    kb1.change_lang()
    assert kb1.language == "EN"


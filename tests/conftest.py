import pytest

from oop_blackjack.cards import FrenchCard


@pytest.fixture
def some_card():
    return FrenchCard(1, 'Hearts')


@pytest.fixture
def some_cards():
    return [
        FrenchCard(1, 'Hearts'),
        FrenchCard(13, 'Diamonds'),
        FrenchCard(7, 'Clubs')
    ]


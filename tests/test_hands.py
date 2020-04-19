import pytest

from oop_blackjack.cards import FrenchCard
from oop_blackjack.hands import BaseHand, BlackJackHand


@pytest.fixture
def base_hand():
    return BaseHand()


@pytest.fixture
def black_jack_hand():
    return BlackJackHand()


@pytest.fixture(scope='module')
def some_cards():
    return [
        FrenchCard(1, 'Hearts'),
        FrenchCard(13, 'Diamonds'),
        FrenchCard(7, 'Clubs')
    ]


def test_manip_cards_on_base(base_hand, some_cards):
    """
    check property setting/getting;
    check add method
    """
    base_hand.cards = [
        FrenchCard(1, 'Hearts'),
        FrenchCard(13, 'Diamonds'),
        FrenchCard(7, 'Clubs')
    ]
    assert base_hand.cards == some_cards

    base_hand.add(some_cards[0])
    assert base_hand.cards == some_cards + [some_cards[0]]

    base_hand.cards = list()
    assert base_hand.cards == list()


if __name__ == '__main__':
    pytest.main()

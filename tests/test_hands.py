import pytest

from oop_blackjack.cards import FrenchCard
from oop_blackjack.hands import BaseHand, BlackJackHand


@pytest.fixture
def base_hand():
    return BaseHand()


def test_manip_cards_on_base(base_hand, some_cards):
    """
    check property setting/getting;
    check add method
    """
    for card in some_cards:
        base_hand.add(card)
    assert base_hand.cards == some_cards

    base_hand.add(some_cards[0])
    assert base_hand.cards == some_cards + [some_cards[0]]

    base_hand.clear()
    assert base_hand.cards == list()


def test_hand_eq(base_hand, some_cards):
    for card in some_cards:
        base_hand.add(card)

    other_hand = BaseHand()
    black_jack_hand = BlackJackHand()
    rvrs_cards = some_cards[::-1]
    for card in rvrs_cards:
        other_hand.add(card)
        black_jack_hand.add(card)

    assert base_hand.cards == some_cards
    assert other_hand.cards == rvrs_cards == black_jack_hand.cards

    assert base_hand == other_hand
    assert base_hand != black_jack_hand


def test_bj_hand_value_aces():
    phand, dhand = BlackJackHand(), BlackJackHand(dealer=True)

    aoh = FrenchCard(1, 'Hearts')
    for i in range(1, 5):
        phand.add(aoh)
        dhand.add(aoh)

    assert phand == dhand
    assert phand.value == dhand.value == 14


def test_bj_hand_value_general():
    phand = BlackJackHand()
    assert phand.value == 0

    phand.add(FrenchCard(13, 'Spades'))  # king of spades ie face card
    assert phand.value == 10

    phand.add(FrenchCard(12, 'Clubs'))  # face card
    assert phand.value == 20

    phand.add(FrenchCard(1, 'Hearts'))  # ace
    assert phand.value == 21

    phand.clear()
    assert phand.value == 0


def test_bj_hand_comparison():
    h1, h2 = BlackJackHand(), BlackJackHand(dealer=True)

    h1.add(FrenchCard(1, 'Spades'))
    h1.add(FrenchCard(10, 'Clubs'))
    assert h1.value == 21

    h2.add(FrenchCard(5, "Spades"))
    h2.add(FrenchCard(7, 'Diamonds'))
    assert h2.value == 12

    assert h1 > h2

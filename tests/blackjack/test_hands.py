import pytest

from oop_practice.blackjack.cards import FrenchCard
from oop_practice.blackjack.hands import BaseHand, BlackJackHand


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
    for card in some_cards[::-1]:
        other_hand.add(card)
        black_jack_hand.add(card)

    assert base_hand.cards == some_cards
    assert other_hand.cards == black_jack_hand.cards == some_cards[::-1]
    assert base_hand == other_hand

    with pytest.raises(TypeError):
        # cannot compare
        assert base_hand != black_jack_hand


def test_bj_hand_value_aces():
    phand, dhand = BlackJackHand(), BlackJackHand()

    aoh = FrenchCard(1, 'Hearts')
    for i in range(1, 5):
        phand.add(aoh)
        dhand.add(aoh)

    assert phand == dhand
    assert phand.value == dhand.value == 14


def test_bj_hand_value_general():
    hand = BlackJackHand()
    assert hand.value == 0

    hand.add(FrenchCard(13, 'Spades'))  # king of spades ie face card
    assert hand.value == 10

    hand.add(FrenchCard(12, 'Clubs'))  # face card
    assert hand.value == 20

    hand.add(FrenchCard(1, 'Hearts'))  # ace
    assert hand.value == 21

    hand.clear()
    assert hand.value == 0


def test_bj_hand_properties():
    hand = BlackJackHand()
    assert hand == 0

    hand.add(FrenchCard(1, 'Spades'))
    assert len(hand) == 1
    assert hand == 11
    assert hand.contains_ace
    assert not hand.busted
    assert not hand.natural_blackjack
    assert not hand.soft

    hand.add(FrenchCard(12, 'Clubs'))  # face card value of 10
    assert len(hand) == 2
    assert hand == 21
    assert hand.contains_ace
    assert not hand.busted
    assert hand.natural_blackjack
    assert hand.soft

    hand.add(FrenchCard(10, 'Hearts'))
    assert len(hand) == 3
    assert hand == 21
    assert hand.contains_ace
    assert not hand.busted
    assert not hand.natural_blackjack
    assert not hand.soft

    hand.add(FrenchCard(1, 'Hearts'))
    assert len(hand) == 4
    assert hand == 22
    assert hand.contains_ace
    assert hand.busted
    assert not hand.natural_blackjack
    assert not hand.soft

    hand.clear()
    assert len(hand) == 0
    assert hand == 0


def test_bj_hand_comparison():
    hand1, hand2 = BlackJackHand(), BlackJackHand()

    hand1.add(FrenchCard(10, 'Clubs'))
    assert hand1 == 10

    hand2.add(FrenchCard(5, "Spades"))
    hand2.add(FrenchCard(5, 'Diamonds'))
    assert hand2 == 10

    assert hand1 == hand2

    hand1.add(FrenchCard(1, 'Hearts'))
    assert hand1 == 21

    # check all the comparisons
    assert hand1 > hand2
    assert hand1 >= hand2
    assert hand2 < hand1
    assert hand2 <= hand1
    assert hand2 != hand1
    assert hand2 == hand2

    # now check natural blackjack vs hand value of 21
    hand2.add(FrenchCard(1, 'Spades'))
    assert hand2 == 21
    assert not hand2.natural_blackjack

    assert hand2 < hand1
    assert hand1 > hand2

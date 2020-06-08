import pytest
import random

from oop_practice.blackjack.cards import FrenchCard


def test_set_properties(some_card):
    some_card.rank = FrenchCard.valid_ranks[0]
    some_card.suit = FrenchCard.valid_suits[0]

    # try to set values outside valid ranges
    with pytest.raises(ValueError):
        some_card.rank = 100

    with pytest.raises(ValueError):
        some_card.suit = 'This does not work'


def test_props_ok(some_card):
    some_card.rank = random.choice(FrenchCard.valid_ranks)
    some_card.suit = random.choice(FrenchCard.valid_suits)


def test_repr_rank():
    assert repr(FrenchCard(1, 'Hearts')) == 'Ace of Hearts'
    assert repr(FrenchCard(10, 'Spades')) == '10 of Spades'


# def test_card_equality():
#     x = FrenchCard(1, 'Hearts')
#     y = FrenchCard(13, 'Hearts')
#     z = FrenchCard(1, 'Clubs')
#
#     assert x < y
#     assert z < y
#     assert x == z
#     assert x != 1
#     assert y != 13 and y != 10

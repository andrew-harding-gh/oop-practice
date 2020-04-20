import pytest
import random

from oop_blackjack.cards import FrenchCard


def test_props_fail(some_card):
    with pytest.raises(ValueError):
        some_card.rank = 100

    with pytest.raises(ValueError):
        some_card.suite = 'This does not work'


def test_props_ok(some_card):
    some_card.rank = random.choice(FrenchCard.valid_ranks)
    some_card.suite = random.choice(FrenchCard.valid_suites)


def test_repr_rank():
    assert repr(FrenchCard(1, 'Hearts')) == 'Ace of Hearts'
    assert repr(FrenchCard(10, 'Spades')) == '10 of Spades'


def test_eq():
    x = FrenchCard(1, 'Hearts')
    y = FrenchCard(1, 'Hearts')
    z = FrenchCard(1, 'Clubs')

    assert x is not y
    assert x == y != z

    with pytest.raises(TypeError):
        # not implemented
        assert x > y

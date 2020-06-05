import pytest

from oop_practice.blackjack.cards import FrenchCard
from oop_practice.blackjack.decks import BaseDeck, FrenchDeck, CasinoDeck


@pytest.fixture
def deck():
    return BaseDeck()


@pytest.fixture
def french_deck():
    return FrenchDeck()


@pytest.fixture
def casino_deck():
    return CasinoDeck()


def test_deck_init(deck):
    assert isinstance(deck, BaseDeck)
    assert deck.cards == list()
    # ensure non-pick methods work on empty deck
    deck.cut()
    deck.shuffle()


def test_pick_from_empty_base_deck(deck):
    with pytest.raises(ValueError):
        deck.pick()


def test_french_deck_init(french_deck):
    # ensure inheritance is good
    assert isinstance(french_deck, FrenchDeck)
    assert issubclass(FrenchDeck, BaseDeck)

    assert len(french_deck.cards) == 52
    for c in french_deck.pick(3):
        assert_card_is_french_card(c)


def test_casino_deck_init(casino_deck):
    # ensure inheritance
    assert isinstance(casino_deck, FrenchDeck)
    assert issubclass(CasinoDeck, FrenchDeck)
    assert issubclass(CasinoDeck, BaseDeck)

    assert len(casino_deck) == 8 * 52  # default param for num of decks is 8
    for c in casino_deck.pick(3):
        assert_card_is_french_card(c)


# utility
def assert_card_is_french_card(card):
    assert isinstance(card, FrenchCard)
    assert hasattr(card, 'rank')
    assert hasattr(card, 'suite')

import pytest

from oop_blackjack.abstracts import AbstractCard, AbstractDeck
from oop_blackjack.cards import FrenchCard
from oop_blackjack.decks import Deck, FrenchDeck, CasinoDeck


@pytest.fixture
def deck():
    return Deck()


@pytest.fixture
def french_deck():
    return FrenchDeck()


@pytest.fixture
def casino_deck():
    return CasinoDeck()


def test_deck_init(deck):
    assert isinstance(deck, Deck)
    assert issubclass(Deck, AbstractDeck)
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
    assert issubclass(FrenchDeck, Deck)
    assert issubclass(FrenchDeck, AbstractDeck)

    assert len(french_deck.cards) == 52
    for c in french_deck.pick(3):
        assert_card_is_french_card(c)


def test_casino_deck_init(casino_deck):
    # ensure inheritance
    assert isinstance(casino_deck, FrenchDeck)
    assert issubclass(CasinoDeck, FrenchDeck)
    assert issubclass(CasinoDeck, Deck)
    assert issubclass(CasinoDeck, AbstractDeck)

    assert len(casino_deck) == 8 * 52  # default param for num of decks is 8
    for c in casino_deck.pick(3):
        assert_card_is_french_card(c)


# utility
def assert_card_is_french_card(card):
    assert isinstance(card, FrenchCard)
    assert hasattr(card, 'rank')
    assert hasattr(card, 'suite')

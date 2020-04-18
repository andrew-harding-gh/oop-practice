from random import shuffle as rnd_shuffle  # in-place shuffling

from oop_blackjack.abstracts import AbstractDeck, AbstractCard
from oop_blackjack.cards import FrenchCard


class Deck(AbstractDeck):
    def __init__(self):
        self.cards = self._init_deck()

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        if not isinstance(value, list) or not all(isinstance(c, AbstractCard) for c in value):
            raise ValueError('Can only set cards to be a list of Card instances')
        self._cards = value

    def shuffle(self):
        rnd_shuffle(self.cards)

    def pick(self, n=1):
        """
        n: int >= 1
        Returns cards: list of FrenchCard instances
        """
        if not self.cards:
            raise ValueError('Cannot pick from  an empty deck')
        if n > len(self.cards):
            raise ValueError('Cannot pick more cards than are available')
        cards = self.cards[:n]
        del self.cards[:n]
        return cards

    def cut(self):
        mid = len(self.cards) // 2
        self.cards = self.cards[mid:] + self.cards[:mid]


class FrenchDeck(Deck):
    """
    Deck one would normally think of, 52 cards consisting of 4 suites, Ace through King
    """

    def __init__(self):
        Deck.__init__(self)
        self.cards = self._init_deck()

    def _init_deck(self):
        deck = [
            FrenchCard(rank, suite)
            for rank in FrenchCard.valid_ranks
            for suite in FrenchCard.valid_suites
        ]
        rnd_shuffle(deck)  # in-place
        return deck


class CasinoDeck(FrenchDeck):
    """ x-count FrenchDecks shuffled together """

    def __init__(self, x=8):
        Deck.__init__(self)
        self.cards = self.cards * x
        self.shuffle()

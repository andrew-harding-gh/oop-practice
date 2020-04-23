from abc import abstractmethod
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
            raise TypeError('Can only set cards to be a list of Card instances')
        self._cards = value

    @abstractmethod
    def _init_deck(self):
        return list()

    def shuffle(self):
        rnd_shuffle(self.cards)

    def pick(self, n=1):
        """
        n: int >= 1
        Returns cards: list of FrenchCard instances
        """
        if not self.cards:
            raise ValueError('Cannot pick from an empty deck')
        if n > len(self.cards):
            raise ValueError('Cannot pick more cards than are available')
        cards = self.cards[:n]
        del self.cards[:n]
        return cards

    def deal(self):
        """ wrapper to only return a Card instance """
        return self.pick(n=1)[0]

    def cut(self):
        mid = len(self.cards) // 2
        self.cards = self.cards[mid:] + self.cards[:mid]

    def __len__(self):
        return len(self.cards)


class FrenchDeck(Deck):
    """
    Deck one would normally think of, 52 cards consisting of 4 suites, Ace through King
    """

    def __init__(self):
        Deck.__init__(self)
        self.cards = self._init_deck()

    @property
    def pcent_remain(self):
        """ :returns 0 <= int <= 100 """
        return int(round(len(self) / 52))

    def _init_deck(self):
        deck = [
            FrenchCard(rank, suite)
            for rank in FrenchCard.valid_ranks
            for suite in FrenchCard.valid_suites
        ]
        rnd_shuffle(deck)  # in-place
        return deck


class CasinoDeck(FrenchDeck):
    """ num_decks-count FrenchDecks shuffled together """

    def __init__(self, num_decks=8):
        Deck.__init__(self)
        self.num_decks = num_decks
        self.cards = self.cards * self.num_decks
        self.shuffle()

    @property
    def pcent_remain(self):
        """ :returns 0 <= int <= 100 """
        return int(round(len(self) / (self.num_decks * 52) * 100))

from random import shuffle as rnd_shuffle  # in-place shuffling
from collections.abc import MutableSequence

from oop_practice.blackjack.abstracts import AbstractCard
from oop_practice.blackjack.cards import FrenchCard


class BaseDeck(MutableSequence):

    def __init__(self):
        self._cards = self._init_deck()

    def __getitem__(self, i: int):
        return self.cards[i]

    def __setitem__(self, i: int, value) -> None:
        self.cards[i] = value

    def __delitem__(self, i: int) -> None:
        del self.cards[i]

    def __len__(self) -> int:
        return len(self.cards)

    def __contains__(self, item):
        return item in self.cards

    def insert(self, index: int, value) -> None:
        self.cards.insert(index, value)

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        if not isinstance(value, list):
            raise TypeError('Can only set cards to be a list of Card instances')
        elif not all(isinstance(c, AbstractCard) for c in value):
            raise TypeError(f'All elements of the target list must implement the `{AbstractCard.__name__}` interface')
        self._cards = value

    def _init_deck(self):
        return list()

    def shuffle(self):
        rnd_shuffle(self.cards)

    def pick(self, n=1):
        """
        n: int >= 1
        Returns cards: list of FrenchCard instances
        """
        if not self:
            raise ValueError('Cannot pick from an empty deck')
        if n > len(self):
            raise ValueError('Cannot pick more cards than are available')
        cards = self[:n]
        del self[:n]
        return cards

    def cut(self):
        mid = len(self.cards) // 2
        self.cards = self.cards[mid:] + self.cards[:mid]


class FrenchDeck(BaseDeck):
    """
    Deck one would normally think of, 52 cards consisting of 4 suits, Ace through King
    """

    def __init__(self):
        BaseDeck.__init__(self)
        self.cards = self._init_deck()

    @property
    def percent_remain(self):
        """ :returns 0 <= int <= 100 """
        return int(round(len(self) / 52 * 100))

    def _init_deck(self):
        deck = [
            FrenchCard(rank, suit)
            for rank in FrenchCard.valid_ranks
            for suit in FrenchCard.valid_suits
        ]
        rnd_shuffle(deck)  # in-place
        return deck


class CasinoDeck(FrenchDeck):
    """ num_decks-count FrenchDecks shuffled together """

    def __init__(self, num_decks=8):
        BaseDeck.__init__(self)
        self.num_decks = num_decks
        self.cards = self.cards * self.num_decks  # we don't care about obj id equivalence for cards
        self.shuffle()

    @property
    def percent_remain(self):
        """ :returns 0 <= int <= 100 """
        return int(round(len(self) / (self.num_decks * 52) * 100))

import operator
from collections.abc import MutableSequence
from functools import total_ordering
from numbers import Number

from oop_practice.blackjack.abstracts import AbstractCard


class BaseHand(MutableSequence):
    def __init__(self):
        self._cards = list()

    def __delitem__(self, i: int) -> None:
        del self.cards[i]

    def __getitem__(self, i: int):
        return self.cards[i]

    def __setitem__(self, i: int, value) -> None:
        self.cards[i] = value

    def __repr__(self):
        return str(self.cards)

    def __eq__(self, other):
        """equivalent if both contain all the same cards and are of the same Hand type"""
        if isinstance(other, self.__class__):
            return all(
                card == ocard
                for (card, ocard)
                in tuple(zip(
                    sorted(self.cards, key=operator.attrgetter('rank')),
                    sorted(other.cards, key=operator.attrgetter('rank'))
                ))
            )
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iter__(self):
        yield from self.cards

    def __len__(self):
        return len(self.cards)

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        if not isinstance(value, list):
            raise TypeError('Can only set cards to be a list of Cards')
        if not all(isinstance(c, AbstractCard) for c in value):
            raise TypeError(f'All elements of the target list must implement the `{AbstractCard.__name__}` interface')
        self._cards = value

    def insert(self, index: int, value) -> None:
        self.cards[index] = value

    def add(self, card):
        if not isinstance(card, AbstractCard):
            raise TypeError('Can only add AbstractCard instances to Hand')
        self._cards.append(card)

    def clear(self):
        self.cards.clear()


@total_ordering
class BlackJackHand(BaseHand):
    """
    dealer: boolean -> if hand belongs to dealer BlackJackPlayer
    """

    rank_conversion = {11: 10, 12: 10, 13: 10, 1: 11}

    def __init__(self):
        BaseHand.__init__(self)

    # TODO: soft/hard property
    @property
    def soft(self):
        return len(self) == 2 and self.contains_ace

    @property
    def contains_ace(self):
        return any([c.rank == 1 for c in self])

    @property
    def busted(self):
        return self.value > 21

    @property
    def value(self):
        num_aces = 0
        value = 0
        for card in self:
            if card.rank == 1:
                num_aces += 1
            value += BlackJackHand.rank_conversion.get(card.rank, card.rank)
        i = 0
        while i < num_aces and value > 21:
            value -= 10
            i += 1

        return value

    @property
    def natural_blackjack(self):
        """ if hand is a 'blackjack' this will beat out other hands of value 21 """
        return self.value == 21 and len(self.cards) == 2

    def dealer_repr(self):
        return str(["Hidden"] + self.cards[1:])

    def __eq__(self, other):
        """ equivalent if hand value is the same and are both BlackJack type Hands"""
        if isinstance(other, Number):
            return self.value == other
        if isinstance(other, self.__class__):
            return self.value == other.value and self.natural_blackjack == other.natural_blackjack
        raise TypeError(f'Cannot compare object of type {type(other)} to {self.__class__}')

    def __lt__(self, other):
        if isinstance(other, Number):
            return self.value < other
        if isinstance(other, self.__class__):
            return self.value < other.value or (not self.natural_blackjack and other.natural_blackjack)
        raise TypeError(f'Cannot compare object of type {type(other)} to {self.__class__}')

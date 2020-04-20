import operator
from functools import total_ordering

from oop_blackjack.abstracts import AbstractHand, AbstractCard


class BaseHand(AbstractHand):
    def __init__(self):
        self._cards = list()

    @property
    def cards(self):
        return self._cards

    def add(self, card):
        if not isinstance(card, AbstractCard):
            raise TypeError('Can only add AbstractCard instances to Hand')
        self._cards.append(card)

    def clear(self):
        self.cards.clear()

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


@total_ordering  # fill orderings from eq and one operator
class BlackJackHand(BaseHand):
    """
    dealer: boolean -> if hand belongs to dealer Player
    """

    rank_conversion = {11: 10, 12: 10, 13: 10, 1: 11}

    def __init__(self, dealer=False):
        BaseHand.__init__(self)
        self._dealer = dealer

    @property
    def value(self):
        # dynamically calc each time its called
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

    def __repr__(self):
        if self._dealer:
            return str(["Hidden"] + self._cards[1:])
        return BaseHand.__repr__(self)

    def __eq__(self, other):
        """ equivalent if hand value is the same and are both BlackJack type Hands"""
        if isinstance(other, self.__class__):
            return self.value == other.value
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.value < other.value

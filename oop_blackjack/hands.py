from oop_blackjack.abstracts import AbstractHand, AbstractCard


# TODO: implement __iter__ ?
class BaseHand(AbstractHand):
    def __init__(self):
        self.cards = list()

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, card_list):
        if not isinstance(card_list, list) or not all(isinstance(c, AbstractCard) for c in card_list):
            raise ValueError('Cards attribute of BaseHand instances can only consist of a list of Card instances')
        self._cards = card_list

    def add(self, card):
        if not isinstance(card, AbstractCard):
            raise ValueError('Can only add AbstractCard instances to Hand')
        self._cards.append(card)

    def __repr__(self):
        return str(self.cards)

    # TODO: order will matter here, need a dif type of container? or just order
    # def __eq__(self, other):
    #     if isinstance(other, BaseHand):
    #         return all(
    #             card == ocard
    #             for card in self.cards
    #               and ocard in other.cards
    #         )
    #     return False


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
        total = 0
        for card in self._cards:
            total += BlackJackHand.rank_conversion.get(card.rank, card.rank)
            if card.rank == 1 and total > 21:
                total -= 10
        return total

    def __repr__(self):
        if self._dealer:
            return "Hidden" + str(self._cards[1:])
        return BaseHand.__repr__(self)

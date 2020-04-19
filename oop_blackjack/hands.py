from oop_blackjack.abstracts import AbstractHand, AbstractCard


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

    def __repr__(self):
        return str(self.cards)


class BlackJackHand(BaseHand):
    """
    dealer: boolean -> if hand belongs to dealer Player
    """

    rank_conversion = dict.fromkeys([11, 12, 13], 10)

    def __init__(self, dealer=False):
        BaseHand.__init__(self)
        self.dealer = dealer
        self.value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def get_value(self):
        v = 0
        count = len(self.cards)
        if count == 2:
            # TODO
            pass

    def __repr__(self):
        if self.dealer:
            return "Hidden" + self.cards[1:]
        return BaseHand.__repr__(self)

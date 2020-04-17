from abc import ABC, abstractmethod

'''
 A class that has a metaclass derived from ABCMeta cannot be instantiated unless 
 all of its abstract methods and properties are overridden.
'''


class AbstractCard(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @property
    @abstractmethod
    def rank(self):
        pass

    @property
    @abstractmethod
    def suite(self):
        pass


class AbstractDeck(ABC):
    def _init_deck(self):
        return list()

    @property
    @abstractmethod
    def cards(self):
        return self._init_deck()

    @abstractmethod
    def pick(self):
        pass

    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def cut(self):
        pass


class AbstractPlayer(ABC):
    @property
    @abstractmethod
    def hand(self):
        pass

    # @abstractmethod
    # def hit(self):
    #     pass
    #
    # @abstractmethod
    # def stay(self):
    #     pass


# would this work? @TODO
class AbstractHand(ABC):
    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

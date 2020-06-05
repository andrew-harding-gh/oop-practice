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
    def suit(self):
        pass

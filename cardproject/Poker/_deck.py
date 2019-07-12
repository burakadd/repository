from typing import List
from ._card import Card


class Deck:
    __cards: List[Card]

    def __init__(self):
        from random import shuffle
        self.__cards = [
            Card(value, suit) for value in range(Card.MAX_VALUE + 1)
            for suit in range(Card.MAX_SUIT + 1)
        ]
        shuffle(self.__cards)

    def __str__(self):
        return ",".join(map(str, self.__cards))

    def pop(self):
        return self.__cards.pop()

    @property
    def cards(self):
        return tuple(self.__cards)


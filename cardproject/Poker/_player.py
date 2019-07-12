from typing import List
from ._card import Card


class Player:
    __cards: List[Card]
    __index: int

    def __init__(self):
        self.__cards = []

    def add_card(self, card: Card) -> None:
        assert len(self.__cards) < 2
        self.__cards.append(card)

    def reset(self):
        self.__cards.clear()

    def poll(self):
        raise NotImplementedError()

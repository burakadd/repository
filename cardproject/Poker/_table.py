from typing import List, Deque, Iterable
from collections import deque
from ._card import Card
from ._deck import Deck
from ._player import Player


class Table(object):
    __players: Deque[Player]
    __active: List[Player]
    __deck: Deck
    __cards: List[Card]

    def __init__(self, players: Iterable[Player]):
        from random import shuffle
        self.__players = deque(players)
        self.__deck = Deck()
        self.__cards = []
        shuffle(self.__players)

    def rotate(self) -> None:
        self.__players.appendleft(self.__players.pop())
        self.__active = list(reversed(self.__players))
        self.__deck = Deck()
        self.__cards.clear()
        for player in self.__players:
            player.reset()
            player.add_card(self.__deck.pop())
            player.add_card(self.__deck.pop())

    def poll(self) -> None:
        assert len(self.__active) > 1
        for index in range(len(self.__active) - 1, -1, -1):
            player = self.__active[index]
            result = player.poll()
            if not result:
                self.__active.pop(index)
                if len(self.__active) == 1:
                    break

    def add_cards(self, num: int) -> None:
        assert len(self.__cards) + num <= 5
        for i in range(num):
            self.__cards.append(self.__deck.pop())

    def finish(self):
        combinations = ['High Card', 'Pair',
             'Two Pair', 'Trips',
             'Street', 'Flush',
             'Full House', 'Four of a Kind',
             'Straight Flush', 'Royal Flush']
        Stack = [sorted(self.__cards + i.cards) for i in self.__players]


    @property
    def active(self):
        return tuple(self.__active)

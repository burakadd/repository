from ._card import Card
from ._deck import Deck
from ._player import Player
from typing import List, Deque, Iterable
from collections import deque


class Table:
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

    def rotate(self):
        self.__players.appendleft(self.__players.pop())
        self.__active = list(reversed(self.__players))
        self.__deck = Deck()
        self.__cards.clear()
        for player in self.__players:
            player.reset()
            player.add_card(self.__deck.pop())
            player.add_card(self.__deck.pop())

    def poll(self):
        assert len(self.__active) > 1
        for index, player in enumerate(reversed(self.__players)):
            result = player.poll()
            if not result:
                self.__active.pop(index)
                if len(self.__active) == 1:
                    break

    def add_cards(self, number):
        for i in range(number):
            self.__cards.append()
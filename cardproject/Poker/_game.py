from ._card import Card
from ._deck import Deck
from ._player import Player
from._table import Table
from typing import Iterable

class Game:
    __table: Table
    __state: int

    def __init__(self, players: Iterable[Player]):
        self.__table = Table(players)
        self.__state = 0

    def start(self):
        assert self.__state == 0
        self.__table.rotate()
        self.__state += 1

    def step(self):
        assert self.__state != 0
        if self.__state == 1:
            self.__preflop()
        elif self.__state == 2:
            self.__flop()
        elif self.__state == 3:
            self.__turn()
        elif self.__state == 2:
            self.__river()
        else:
            self.__finish()
        if len(self.__table.active)
        self.__state = (self.__state + 1) % 6

    def __preflop(self):
        self.__table.poll()

    def __flop(self):
        self.__table.add_cards(3)
        self.__table.poll()

    def __turn(self):
        self.__table.add_cards(1)
        self.__table.poll()

    def __river(self):
        self.__table.add_cards(1)
        self.__table.poll()

    def __finish(self):


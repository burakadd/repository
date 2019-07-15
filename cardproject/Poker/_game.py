from typing import Optional, Iterable
from ._player import Player
from ._table import Table


class Game(object):
    __table: Table
    __state: int

    def __init__(self, players: Iterable[Player]):
        self.__table = Table(players)
        self.__state = 0

    def start(self) -> None:
        assert self.__state == 0
        self.__table.rotate()
        self.__state += 1

    def step(self) -> Optional[Player]:
        assert self.__state != 0

        if self.__state == 1:
            self.__preflop()
        elif self.__state == 2:
            self.__flop()
        elif self.__state == 3:
            self.__turn()
        elif self.__state == 4:
            self.__river()
        else:
            self.__finish()

        if len(self.__table.active) > 1:
            self.__state = (self.__state + 1) % 6
        else:
            self.__state = 0

        if self.__state == 0:
            return self.__table.active[0]
        else:
            return None

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
        self.__table.finish()

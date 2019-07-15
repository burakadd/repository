from typing import List
from ._card import Card


class Player(object):
	__cards: List[Card]

	def __init__(self):
		self.__cards = []

	@property
	def cards(self):
		return self.__cards

	def add_card(self, card: Card) -> None:
		assert len(self.__cards) < 2
		self.__cards.append(card)

	def reset(self) -> None:
		self.__cards.clear()

	# def poll(self) -> bool:
    #     raise NotImplementedError()



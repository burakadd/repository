values = '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
suits = '♠', '♣', '♦', '♥'


class Card:
    MAX_VALUE = 12
    MAX_SUIT = 3
    def __init__(self, value, suit):
        assert 0 <= value <= self.MAX_VALUE
        assert 0 <= suit <= self.MAX_SUIT
        self.__value = value
        self.__suit = suit

    @property
    def value(self):
        return self.__value

    @property
    def suit(self):
        return self.__suit

    def __str__(self):
        return values[self.value] + suits[self.suit]

    def __sub__(self, other: 'Card'):
        return self.__value - other.__value

    def __eq__(self, other: 'Card'):
        return self - other == 0

    def __ne__(self, other: 'Card'):
        return self - other != 0

    def __lt__(self, other: 'Card'):
        return self - other< 0

    def __le__(self, other: 'Card'):
        return self - other <= 0

    def __gt__(self, other: 'Card'):
        return self - other > 0

    def __ge__(self, other: 'Card'):
        return self - other >= 0


print(Card(0, 0))


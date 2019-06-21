class Card(object):
    rank = tuple(range(2, 11))+('Jack', 'Queen', 'King', 'Ace')
    suit = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

class Deck(object):
    def __init__(self):
        self._deck = [Card(rank, suit) for rank in Card.rank for suit in Card.suit]



print(Card(2, "Spades"))
print(Deck())

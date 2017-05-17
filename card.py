from random import shuffle

class Card:
    def __init__(self):
        self.values = range(1, 14)
        self.suits = ["H", "D", "C", "S"]
        self.deck = []
        self.deck_for_kard = []
        self.index = -1
        self.number = 1
        for value in self.values:
            for suit in self.suits:
                self.deck.append((suit, value))
        shuffle(self.deck)

    def __next__(self):
        temp = self.deck[0]
        self.deck.pop(0)
        temp = str(temp)
        self.deck_for_kard.append(temp)
        return temp
import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        ranks = [
            "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K", "A"
        ]

        suits = ["♠", "♥", "♦", "♣"]

        self.cards = []

        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("Cannot deal from an empty deck")

        return self.cards.pop()

    def deal_hand(self, number):
        if number > len(self.cards):
            raise ValueError("Not enough cards remaining")

        hand = []

        for _ in range(number):
            hand.append(self.deal())

        return hand

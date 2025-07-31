import random

class Card:
    def CardTypes():
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

    def CardValue(playedCard):
        if playedCard[0] in ['Jack', 'Queen', 'King']:
            return 10
        elif playedCard[0] == 'Ace':
            return 11
        else:
            return int(playedCard[0])


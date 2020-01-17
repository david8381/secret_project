import random

class Deck:
    def __init__(self, cardlist):
        if type(cardlist) == int:
            self.cards = list(range(1, cardlist+1))
        elif type(cardlist) == list:
            self.cards = cardlist
    def split(self, position):
        deck1 = Deck(self.cards[:position])
        deck2 = Deck(self.cards[position:])
        return deck1, deck2
    def __repr__(self):
        return str(self.cards)
    def connect(self, deck2):
       deck1 = self.cards
       deck2 = deck2.cards
       jdeck = []
       while len(deck1) + len(deck2) > 0:
            if len(deck1) > 0 and len(deck2) > 0:
                cdeck = random.randint(0,1)
            elif len(deck1) > 0:
                cdeck = 0
            else:
                cdeck = 1
            if cdeck == 0:
                jdeck.append(deck1[0])
                deck1.pop(0)
            else:
                jdeck.append(deck2[0])
                deck2.pop(0)
       return Deck(jdeck)



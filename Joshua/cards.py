import random

class Deck:
    def __init__(self, cardlist):
        if type(cardlist) == int:
            self.cards = list(range(1, cardlist+1))
        elif type(cardlist) == list:
            self.cards = list(cardlist)
    def split_deck(self, position):
        deck1 = Deck(self.cards[:position])
        deck2 = Deck(self.cards[position:])
        return deck1, deck2
    def __repr__(self):
        return str(self.cards)
    def __len__(self):
        return len(self.cards)
    def get_card_list(self):
        return self.cards
    def combine_decks(self, deck2):
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
    def shuffle(self, times, splitPoint):
       shuffled = 0
       d = self
       while times > shuffled:
           d1, d2 = d.split_deck(splitPoint)
           d = d1.combine_decks(d2)
           shuffled = shuffled + 1
       return d
# THIS IS THE END OF THE DECK CLASS!
def combine_decks(self, deck2):
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



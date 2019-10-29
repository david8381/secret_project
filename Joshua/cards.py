class Deck:
    def __init__(self, cardlist):
        self.cards = cardlist 
    def split(self, position):
        deck1 = Deck(self.cards[0:position])
        deck2 = Deck(self.cards[position:])
        return deck1, deck2
    def __repr__(self):
        return str(self.cards)
    def connect(self, deck1, deck2):
        fdeck = zip(deck1, deck2)
        return zip(fdeck)

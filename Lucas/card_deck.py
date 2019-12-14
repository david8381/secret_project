#Create by Lucas Daniels
from random import randint
classes = ["Hearts", "Diamonds", "Spades", "Clubs"]
values = ["2", "3", "4", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def make_deck(): #Something is wrong with this function
    deck = []
    for i in range(0, 2):
        deck.append(Card("joker", "joker"))
    for value in values:
        for card_class in classes:		
            deck.append(Card(value, card_class))
    return deck


def join_decks(deck1, deck2):
    deck_len = len(deck1) + len(deck2)
    joined_deck = []
    cp_deck1 = []
    cp_deck2 = []
    for card in deck1:
        cp_deck1.append(card)
    for card in deck2:
        cp_deck2.append(card)
    decks = [cp_deck1, cp_deck2]
    while len(cp_deck1) > 0 or len(cp_deck2) > 0:
        deck = decks[randint(0, 1)]
        if len(deck) > 0:
            joined_deck.append(deck[0])
            deck.pop(0)
    return joined_deck


class Card_deck:
    def __init__(self):
        self.deck = []
        for card in range(0, 52):
            self.deck.append(card)
    def split_deck(self, split_point):
    	return self.deck[:split_point], self.deck[split_point:]
    def __repr__(self):
    	return self.deck 


class Card:
    def __init__(self, value, card_class):
    	self.value = value
    	self.card_class = card_class
    def __repr__(self):
    	return str(self.value + " of " + self.card_class)

if __name__ == "__main__":
    print("This is a demo")
    card_deck = Card_deck()
    deck1, deck2 = card_deck.split_deck(int(raw_input("Where would you like to split the deck?")))
    print("Deck 1")
    print(deck1)
    print(" ")
    print("Deck 2")
    print(deck2)
    print(" ")
    print("Joined Deck")
    print(join_decks(deck1, deck2))

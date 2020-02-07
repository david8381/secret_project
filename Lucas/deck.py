#Created by Lucas Daniels
from random import randint
from matplotlib import pyplot as plt
import numpy as np

np.set_printoptions(linewidth=1000, threshold=52**2)

classes = ["Hearts", "Diamonds", "Spades", "Clubs"]
values = ["2", "3", "4", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def combine_decks(deck1, deck2):
    deck_len = len(deck1.deck) + len(deck2.deck)
    joined_deck = []
    cp_deck1 = []
    cp_deck2 = []
    for card in deck1.deck:
        cp_deck1.append(card)
    for card in deck2.deck:
        cp_deck2.append(card)
    decks = [cp_deck1, cp_deck2]
    while len(cp_deck1) > 0 or len(cp_deck2) > 0:
        deck = decks[randint(0, 1)]
        if len(deck) > 0:
            joined_deck.append(deck[0])
            deck.pop(0)
    return Deck(joined_deck)


def shuffle(loops, split, d):
    for i in range(0, loops):
        d1, d2 = d.split_deck(split)
        d = combine_decks(d1, d2)
    return d


def make_array(list_of_decks):
    number_of_decks = len(list_of_decks)
    deck_length = len(list_of_decks[0])
    array = np.zeros(deck_length**2)
    array = array.reshape(deck_length, deck_length)
    for x, deck in enumerate(list_of_decks):
        for y, card in enumerate(deck.deck):
            array[card, y] += 1
    for x, row in enumerate(array):
        for y, column in enumerate(row):
            array[x, y] = array[x, y]/number_of_decks
    return array


def display_array(array): #This function needs work
    for deck in array:
        plt.scatter(range(0, len(deck)), deck)
    plt.show()


class Deck:
    def __init__(self, cards=range(1, 53)):
        self.deck = []
        for card in cards:
            self.deck.append(card)
    def get_card_list(self):
        return self.deck
    def split_deck(self, split_point):
    	return Deck(self.deck[:split_point]), Deck(self.deck[split_point:])
    def display(self):
        plt.scatter(range(0, len(self.deck)), self.deck)
    def __len__(self):
        return len(self.deck)
    def __repr__(self):
    	return str(self.deck)


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

import sys
from deck import Deck, combine_decks

def get_cards():
    card_suits = ['H', 'S', 'C', 'D']
    card_denominations = ['A', 'K', 'Q', 'J'] + [str(x) for x in range(2, 11)]
    cards = [x + y for x in card_suits for y in card_denominations]
    return cards

if __name__ == '__main__':

    test_failed = False

    card_list = get_cards()
    deck = Deck(card_list)

    try:
        assert(len(deck) == len(card_list))
    except AssertionError:
        test_failed = True
        print('Initial Deck Wrong Length')

    try:
        assert(set(deck.get_card_list()) == set(card_list))
    except AssertionError:
        test_failed = True
        print('Initial Deck Wrong Cards')

    deck_1, deck_2 = deck.split_deck(len(card_list)//2)

    try:
        assert(len(deck_1) + len(deck_2) == len(deck))
    except AssertionError:
        test_failed = True
        print('Length of Split Decks Incorrect')

    try:
        assert(set(deck_1.get_card_list()) | set(deck_2.get_card_list()) == set(deck.get_card_list()))
    except AssertionError:
        test_failed = True
        print('Card list of split decks incorrect')

    new_deck = combine_decks(deck_1, deck_2)

    try:
        assert(len(new_deck) == len(deck))
    except AssertionError:
        test_failed = True
        print('Length of combined deck incorrect')

    try:
        assert(set(new_deck.get_card_list()) == set(card_list))
    except AssertionError:
        test_failed = True
        print('card list of combined deck incorrect.')

    if not test_failed:
        print('Congrats -- all tests passed!')




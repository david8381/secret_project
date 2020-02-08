import deck


def get_shuffle_num(D, error_bar, min_cards=-1, deck_num=10000):
    if min_cards==-1:
        min_cards=len(D.deck)**2
    shuffle_num_found = False
    current_shuffle_num = 0
    right_value = len(D.deck)/len(D.deck)**2
    print("#"*100)
    print(f"Shuffling {deck_num} decks of {len(D.deck)} cards. Has \"right value\" of {right_value}")
    print("Current Shuffle:")
    while shuffle_num_found == False:
        print("\b", current_shuffle_num)
        list_of_decks = deck.create_list_of_decks(n=deck_num, shuffle_num=current_shuffle_num, D=D)
        array = deck.make_array(list_of_decks)
        num_within_error_bar = 0
        for row in array:
            for value in row:
                if right_value+error_bar > value > right_value-error_bar:
                    #print(right_value+error_bar, value, right_value-error_bar)
                    num_within_error_bar += 1
        if num_within_error_bar >= min_cards:
            print(f"Success! A deck of {len(D.deck)} needs to be shuffled {current_shuffle_num} times in order for {min_cards} of the valuess to be within {error_bar} of the \"right answer\"")
            return current_shuffle_num
        current_shuffle_num += 1


def plot_shuffle_num(low_deck, high_deck, error_bar=0.005, deck_num=10000):
    results = []
    for i in range(low_deck, high_deck):
        D = deck.Deck(range(i))
        results.append(get_shuffle_num(D, error_bar=error_bar, deck_num=deck_num))
    return results

#Create by Lucas Daniels
classes = ["Hearts", "Diamonds", "Spades", "Clubs"]
values = ["2", "3", "4", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def make_deck():
	deck = []
	for i in range(0, 2):
		deck.append(Card("joker", "joker"))
	for value in values:
		for card_class in classes:		
			deck.append(Card(value, card_class))
	return deck


class Card_deck:
	def __init__(self):
		self.deck = make_deck()
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

card_deck = Card_deck()
deck1, deck2 = card_deck.split_deck(int(raw_input("Where would you like to split the deck?")))

print "Deck 1"
print deck1
print "Deck 2"
print deck2

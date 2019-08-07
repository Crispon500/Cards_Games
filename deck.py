from random import *

class Card:
	def __init__(self,suit,value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:
	valid_suits = ("Hearts", "Diamonds", "Clubs", "Spades")
	valid_values = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
	def __init__(self):
		self.cards = []
		for suit in Deck.valid_suits:
			for value in Deck.valid_values:
				self.cards.append(Card(suit=suit,value=value))

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def shuffle(self):
		if(not (len(self.cards) == 52)):
			raise ValueError("Only full decks can be shuffled")
		shuffle(self.cards)

	def _deal(self,num=1):
		dealt_cards = []
		if(not len(self.cards)):
			raise ValueError("All cards have been dealt")

		for i in range(num):
			if(not len(self.cards)):
				break
			dealt_cards.append(self.cards.pop())

		return dealt_cards

	def deal_card(self):
		card = self._deal()
		return card[0]

	def deal_hand(self,num=5):
		return self._deal(num)

	def count(self):
		return len(self.cards)
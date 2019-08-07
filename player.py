class Player:

	def __init__(self,player_no):
		self.hand = []
		self.player_no = player_no
		self.player_value = -1
		self.hand_value = [0]

	def __repr__(self):
		return f"Player {self.player_no} has {len(self.hand)} cards"

	def draw(self,deck,num=1):
		for i in range(num):
			self.hand.append(deck.deal_card())

	def show_hand(self):
		print(self.hand())

	def discard_hand(self):
		self.hand = []
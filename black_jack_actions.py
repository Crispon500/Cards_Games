def hit(player,deck):
	player.draw(deck)
	count_hand(player)
	check_player_values(player)

def count_hand(player):
	values = [0]
	ten_values = ("J","Q","K")
	hand = player.hand
	for card in hand:
		if card.value in ten_values:
			values = [value+10 for value in values]
		elif card.value == "A":
			values_temp = [value+11 for value in values]
			values = [value+1 for value in values]
			for val in values_temp:
				values.append(val)
		else:
			card_value = card.value
			values = [value+int(card_value) for value in values]

	player.hand_value = values

def check_player_values(player):
	valid_values = []
	for val in player.hand_value:
		if val <= 21:
			valid_values.append(val)
	if valid_values:
		player.player_value = max(valid_values)
	else:
		player.player_value = 0

def bet(player):
	print(f"Your Balance: {player.chips}")
	while True:
		if(player.chips == 0):
			print("Nothing to bet")
			return 0
		max = player.chips
		bet = int(input("How much will you bet? "))
		if(bet > max or 0 >= bet):
			print(f"Please place a valid bet.\tYour Balance: {player.chips}")
		else:
			player.chips -= bet
			return bet

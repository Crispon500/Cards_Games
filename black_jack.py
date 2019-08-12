from deck import *
from player import Player
from black_jack_actions import *
import time

def play():
	game = True
	player_wins = 0
	dealer_wins = 0
	deck = Deck()
	deck.shuffle()
	dealer = Player(player_no=0)
	player = Player(player_no=1)

	while(game):
		player.discard_hand()
		dealer.discard_hand()
		pot = bet(player)

		#deal for dealer
		hit(dealer,deck)
		hit(dealer,deck)
		#deal for player
		hit(player,deck)
		hit(player,deck)

		print(f"\nDealer: [Face Down card, {dealer.hand[1]}]")
		print(f"Player 1: {player.hand} for {player.player_value}")

		if player_turn(player,deck):
			dealer_turn(dealer,deck)
		else:
			dealer_wins += 1
			game = play_again()
			continue

		print(f"Player: {player.player_value} \t Dealer: {dealer.player_value}")
		if(player.player_value > dealer.player_value):
			player_wins += 1
			print("PLAYER WINS!!!!!")
			player.chips += pot*2
		elif(player.player_value < dealer.player_value):
			dealer_wins += 1
			print("HOUSE WINS!!!!!")
		else:
			print("PUSH!")
		game = play_again()


def player_turn(player,deck):
	player_turn = True
	while(player_turn):
		input_key = input("Will you hit or stand? (Type Hit or Stand) ")
		if(input_key.lower() == "hit"):
			hit(player,deck)
			print(f"Player 1: {player.hand} for {player.player_value}")
		elif(input_key.lower() == "stand"):
			player_turn = False
		else:
			print("Please, choose a valid option")

		if(not player.player_value):
			player_turn = False
			print("BUST!!!")
			return False
	return True


def dealer_turn(dealer,deck):
	dealer_turn = True
	print(f"Dealer: {dealer.hand} for {dealer.player_value}")
	if(dealer.player_value >= 17):
		dealer_turn = False
	while(dealer_turn):
		time.sleep(2)
		hit(dealer,deck)
		print(f"Dealer: {dealer.hand} for {dealer.player_value}")
		if(dealer.player_value >= 17):
			dealer_turn = False
		if(dealer.player_value == 0):
			print("Dealer Bust!!!")
			dealer_turn = False

def play_again():
	while True:
		play_again = input("\nPlay again? Y/N ")
		if(play_again.upper() == "N"):
			return False
		elif(play_again.upper() == "Y"):
			return True
		else:
			print("Please type \"Y\" or \"N\"")
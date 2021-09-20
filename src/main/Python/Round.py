from Deck import *

class Round(object):
	"""
		
		Each round has a deck
		And a group of player from 2-4 they should come inherited 
			from Game
		Each player has a turn 

	"""
	def __init__(self, players):
		super(Round, self).__init__()
		self.players = players
		self.players_order = []
		self.deck = Deck()

	def sort(self):
		return(self.players_order.reverse())

	def state(self):
		state = "\n\n\n\n"
		for player in self.players:
			state = state +  str(player.name) + " : \t\n"
		state += "\n\n Cards on deck \t" + str(self.deck.state())
		return (state)

	def show(self):
		state = "\n\n\n\n"
		for player in self.players:
			state += player
		return (state)

	def play(self):
 		player = 0
 		winner = None

 		for i in range(0,3):
 			self.deck.pull()

 		for player in self.players:
 			player.current_card = self.deck.pull()

 		while (self.deck.state()!=0):
 			print(self.state())

 			current_card = self.deck.pull()
 			current_player = self.players[player]

 			print("all", "Its the turn of" + current_player)

 			print(current_player,"Pick the card you want to keep, the other one will set the action")
 			picked_card = current_player.play(current_card)

 			print("all", current_player + "put a" + picked_card + " on the table")
 			if(picked_card.name == 'Guard'):
 				print("all","\n Guard allows you to discard one oponent if you guess right the card they have\n")
 				print(current_player,"\n Oponents:")
 				for player in self.players:
 					if(not player.protection and play!=current_player):
 						print("\t" + player)
 				oponent = input("current_player \nPick the oponent:\t")
 				done = True
 				while(done):
	 				for player in self.players:
	 					if(player.name == oponent and not player.protection and play!=current_player):
	 						picked = input("current_player Guess the card:\t")
	 						if(picked=='Guard' or picked=='Priest' or picked=='Baron' or picked=='Handmaid' or picked=='Prince' or picked=='King' or picked=='Countess' or picked=='Princess'):
	 							done = False
	 							print("all", current_player + " chose " + player + " and says that the hidden card is a " + picked)
	 							if(picked==player.current_card.name):
	 								self.players_order.append(self.players.remove(player))
	 								print("all", current_player + " chose guest card correctly. " + player + " is out!")
	 								print(player, "You are out! Wait until the round is over")
	 							else:
	 								print("all", current_player + " chose guest card incorrectly. " + player + " is still on the game!")
	 						else:
	 							print(current_player, "Pick a valid card, options are:\n\t Guard\n\t Priest\n\t Baron\n\t Handmaid\n\t Prince\n\t King\n\t Countess\n\t Princess")
 					if(not done):
 						print(current_player, "Choose a valid player")
 			elif(picked_card.name == 'Priest'):
 				print("all","\n Priest allows you to see an oponent's card\n")
 				print(current_player,"\n Oponents:")
 				for player in self.players:
 					if(not player.protection and play!=current_player):
 						print("\t" + player)
 				oponent = input("current_player \nPick the oponent:\t")
 				done = True
 				while(done):
	 				for player in self.players:
	 					if(player.name == oponent and not player.protection and play!=current_player):
 							print(current_player, player + " has a " + player.current_card)
 							print("all",current_player + " saw " + player + "'s card")
 							done = False
	 				if(not done):
 						print(current_player, "Choose a valid player")
 			elif(picked_card.name == 'Baron'):
 				print("all","\n Baron allows you to check secretly one's card and the lowest one will be out of the game\n")
 				print(current_player,"\n Oponents:")
 				for player in self.players:
 					if(not player.protection and play!=current_player):
 						print("\t" + player)
 				oponent = input("current_player \nPick the oponent:\t")
 				done = True
 				while(done):
	 				for player in self.players:
	 					if(player.name == oponent and not player.protection and play!=current_player):
 							print("all",current_player + " chose " + player)
 							print(current_player, player + " has a " + player.current_card)
 							print(player, current_player + " has a " + current_player.current_card)
 							if(player.current_card.value > current_player.current_card.value):
 								self.players_order.append(self.players.remove(player))
 								print("all", current_player + "'s card had a greater value," + player + " is out!")
 								print(player, "You are out! Wait until the round is over")
 							elif(current_player.current_card.value > player.current_card.value):
 								self.players_order.append(self.players.remove(current_player))
 								print("all", player + "'s card had a greater value," + current_player + " is out!")
 								print(current_player, "You are out! Wait until the round is over")
 							else:
 								print("all", player + " and " + current_player + " have the same card's no one is out!")
 							done = False
	 				if(not done):
 						print(current_player, "Choose a valid player")
 			elif(picked_card.name == 'Handmaid'):
 				print("all","\n Handmaid gives you protection from others cards until your next turn\n")
 				current_player.protection = True
 				print(current_player, "Your protection is now activated until next turn")
 			elif(picked_card.name == 'Prince'):
 				print("all","\n Prince allows you to make someone discard the card they have and pull a new one\n")
 				print(current_player,"\n Oponents:")
 				for player in self.players:
 					if(not player.protection):
 						print("\t" + player)
 				oponent = input("current_player \nPick the oponent:\t")
 				done = True
 				while(done):
	 				for player in self.players:
	 					if(player.name == oponent and not player.protection):
 							print("all",current_player + " chose " + player )
 							player.used_cards.append(current_card)
 							player.current_card = self.deck.pull()
 							print(player, "You have a new card now and is a " + player.current_card)
 							print("all", player + "has a new card")
 							done = False
	 				if(not done):
 						print(current_player, "Choose a valid player")
 			elif(picked_card.name == 'King'):
 				print("all","\n King allows you exchage your cards with an oponent\n")
 				print(current_player,"\n Oponents:")
 				for player in self.players:
 					if(not player.protection and play!=current_player):
 						print("\t" + player)
 				oponent = input("current_player \nPick the oponent:\t")
 				done = True
 				while(done):
	 				for player in self.players:
	 					if(player.name == oponent and not player.protection and play!=current_player):
	 						current_player.current_card, player.current_card = player.current_card, current_player.current_card
 							print(current_player, "Your new card is " + player.current_card)
 							print(player, "Your new card is " + current_player.current_card)
 							print("all",current_player + " exchanged with " + player)
 							done = False
	 				if(not done):
 						print(current_player, "Choose a valid player")
 			elif(picked_card.name == 'Countess'):
 				print("all","\n Countess has no action\n")
 			elif(picked_card.name == 'Princess'):
 				print("all", "\n If Princess is discarted to are out of the round")
 				self.players_order.append(self.players.remove(current_player))
 				print("all", current_player + "has left the round")
 				print(player, "You are out! Wait until the round is over")
 			player = (player+1)%len(self.players)
 			if(len(self.players)==0):
 				break
 		print(self.show())

 		#Evaluate who wins:
 		for player in self.players:
 			values = [player.current_card.value for player in self.players]
 			winner_value = max(values)
 			if(values.count(winner_value)==1):
	 			winner = values.index(winner_value)
 				self.players[winner].wins_counter += 1
 				print("Winner is" + self.players[winner])
 			else:
 				print("Is a tie! No one wins") 
 		return (self.sort())
		
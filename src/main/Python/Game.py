from Round import *

class Game(object):
	"""

       Each game has many round until one player wins

       2 players -> 7 tokens to win
       3 players -> 5 tokens to win
       4 players -> 4 tokens to win

	"""
	def __init__(self, players):
		super(Game, self).__init__()
		self.players = players
		
	def evaluate(self):
		for player in self.players:
			if(len(self.players)==2):
				if(player.wins_counter==7):
					return True
			elif(len(self.players)==3):
				if(player.wins_counter==5):
					return True
			elif(len(self.players)==4):
				if(player.wins_counter==4):
					return True
		return False

	def state(self):
		state = "TABLE AFTER THE GAME:\n"
		for player in self.players:
			state += "\tPlayer: " + player.name + " Tokens: " + str(player.wins_counter) + "\n"
		return state

	def play(self):
		while(not self.evaluate()):
			current = Round(self.players)
			current.play()
			for player_ in self.players:
				player_.client.send('{}'.format(self.state()).encode('ascii'))
from Game import *

class Room(object):
	"""docstring for Room"""

	def __init__(self, _id):
		super(Room, self).__init__()
		self._id = _id
		self.players = []
		self.admin = None

	def join(self, player):
		self.players.append(player)
		if(not self.admin):
			self.admin = player
		print("all", player + " joined the room")

	def remove(self, player):
		self.players.remove(player)
		print("all", player + " is gone")

	def play(self):
		play_now = False
		while(not play_now):
			start = False
			while(not start):
				if(input("admin start")):
					if(len(self.players) >= 2 and len(self.players) <= 4):
						start = True
					else:
						print("admin", "wait for more players to join the room")
			game = Game(self.players)
			game.play()
			if(input("admin play a new game")):
				play_now = True
			


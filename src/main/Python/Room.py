from Game import *

class Room(object):
	"""docstring for Room"""

	def __init__(self, _id):
		super(Room, self).__init__()
		self._id = _id
		self.isPlaying = False
		self.players = []
		self.admin = None

	def join(self, player):
		if(len(self.players)==4):
			player.client.send("The room is full".encode('ascii'))
			return(0)
		player.room = self
		self.players.append(player)
		if(not self.admin):
			self.admin = player
		for player_ in self.players:
			if(player_==player):
				player_.client.send("You are in the room with id {} now".format(self._id).encode('ascii'))
			else:
					player_.client.send("{} joined the room".format(player).encode('ascii'))

	def remove(self, player):
		self.players.remove(player)
		player_.client.send("{} left the room".format(player).encode('ascii'))

	def play(self):
		start = False
		while(not start):
			self.admin.client.send('\nYou are the admin of the room \npress "s" to start the game'.encode('ascii'))   
			admin_choice = self.admin.client.recv(1024).decode('ascii') 
			if(admin_choice=="s"):
				if(len(self.players) >= 2 and len(self.players) <= 4):
					for player_ in self.players:
						player_.client.send("{} started the game".format(self.admin).encode('ascii'))
					game = Game(self.players)
					self.isPlaying = True
					game.play()
				else:
					self.admin.client.send("wait for more players to join the room ".encode('ascii'))
			else:
				for player_ in self.players:
					player_.room = None
				self.players = []
				player_.client.send("{} destroyed the room".format(self.admin).encode('ascii'))

			
			


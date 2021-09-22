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
		self.players.pop(self.players.index(player))
		player_.client.send("{} left the room".format(player).encode('ascii'))

	def play(self):
		self.admin.client.send('\nYou are the admin of the room \npress "s" to start the game and x to kill the room'.encode('ascii'))   
		start = False
		admin_choice = self.admin.client.recv(1024).decode('ascii') 
		while(not start):
			if(admin_choice=="s"):
				if(len(self.players) >= 2 and len(self.players) <= 4):
					for player_ in self.players:
						player_.client.send("{} started the game".format(self.admin).encode('ascii'))
					game = Game(self.players)
					self.isPlaying = True
					game.play()
					return(self.players)
				else:
					self.admin.client.send("wait for more players to join the room ".encode('ascii'))
			if(admin_choice=="x"):
				for player_ in self.players:
					player_.room = None
				self.players = []
				player_.client.send("{} destroyed the room".format(self.admin).encode('ascii'))
				return ([])
#			if(admin_choice=="c"):				#Probably an option to chat
		for player_ in self.players:
			player_.client.send('\n ++++++++++ GAME OVER ++++++++++'.encode('ascii'))
		return(self.players)


			
			


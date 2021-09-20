class Player(object):
	"""
		Each player has a curret card
		Each player has used cards
		Each player has a wins counter
	"""

	def __init__(self, name, client):
		super(Player, self).__init__()
		self.name = name
		self.used_cards = []
		self.current_card = None
		self.wins_counter = 0
		self.client = client
		self.room = None
		self.protection = False					#When you play a handmaid this value is setted to true

	def reset(self):
		self.protection = False
		self.wins_counter = 0
		self.current_card = None
		self.used_cards = []

	def play(self, current_card):
		picked = None
		while(picked != self.current_card.name or picked != current_card.name):
			picked = input("me", "\n Choose wich card do you want to keep, the other will be played on the table\n\t" + self.current_card + "\n\t" + current_card)
			if(picked == self.current_card.name):
				self.used_cards.append(current_card)
				return (current_card)
			else:
				self.used_cards.append(self.current_card)
				self.current_card, current_card = current_card, self.current_card
				return(current_card)

	def __str__ (self):
		toReturn = "User: " + self.name + "\nCards on table:\n"
		for card in self.used_cards:
			toReturn += card
		return (toReturn)
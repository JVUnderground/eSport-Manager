#team.py
class Team(object):
	games = []
	def __init__(self, name):
		self.name = name
		
	def add_game(self, game):
		self.games.append(game)

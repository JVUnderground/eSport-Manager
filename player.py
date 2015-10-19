#player.py
import sqlite3
import os
class Player(object):
	def __init__(self, name, game, position, attributes):
		self.name = name
		self.game = game
		self.position = position
		self.attributes = attributes
	
	def add_position(position):
		self.position.append(position)
		
	def save_player_to_db(self, savepath):
		print "Saving to db %s" % (savepath + os.sep + 'players.db')
		conn = sqlite3.connect(savepath + os.sep + 'players.db')
		c = conn.cursor()
		print (self.name, self.game, self.positions)
		c.execute('INSERT INTO players VALUES (?,?,?)', (self.name, self.game, self.positions))
		conn.commit()
		conn.close()
	
def open_player_from_db(savepath, name):
	conn = sqlite3.connect(savepath + os.sep + 'players.db')
	c = conn.cursor()
	player = ''
	for row in c.execute('SELECT * FROM players WHERE name=\'%s\'' % (name)):
		name = row[0]
		game = row[1]
		position = row[2]
		attributes = { 'roaming' 		: row[3],
					   'positioning'	: row[4],
					   'mechanics'		: row[5],
					   'knowledge'		: row[6],
					   'awareness'		: row[7],
					   'morale'			: row[8],
					   'fitness'		: row[9],
					   'tiredness'		: row[10],
					   'leadership'		: row[11],
					   'judgement'		: row[12],
					   'aggression'		: row[13],
					   'warding'		: row[14],
					   'personality'	: row[15],
					   'sympath'		: row[16]}
		player = Player(name, game, position, attributes)
	return player
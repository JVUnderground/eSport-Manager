#combat.py
import random
class Combat(object):
	def __init__(self, playerA, playerB):
		self.playerA = playerA
		self.playerB = playerB
		self.killcount_A = 0
		self.killcount_B = 0
		
	def solo(self):
		score_A = self.solo_score(self.playerA) + self.killcount_A
		rand_A = random.uniform(0.5,1)
		score_B = self.solo_score(self.playerB) + self.killcount_B
		rand_B = random.uniform(0.5,1)
		if rand_A*score_A > rand_B*score_B:
			self.killcount_A = self.killcount_A + 1
			return self.playerA
		elif rand_B*score_B > rand_A*score_A:
			self.killcount_B = self.killcount_B + 1
			return self.playerB
		else:
			return "no winner"
		
	def solo_score(self, player):
		att = player.attributes
		score = att['positioning'] + att['mechanics'] + att['knowledge'] + att['judgement']
		return score
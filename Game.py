


class Hanoi:
	def __init__(self, rings):
		self.numRings = rings
		self.towers = 3

		self.tower1 = []
		self.tower2 = []
		self.tower3 = []

		for x in range(self.numRings):
			self.tower1.append(x + 1)
			self.tower2.append(0)


	def print_board(self):
		for x in range(self.numRings):
			print("   |      |      |   ")
			print("   " + display(self.tower1[x]));
		print("   |      |      |   ")
		print("_____________________")

def display(num):
	if (num == 0):
		return "|"
	else:
		return str(num)

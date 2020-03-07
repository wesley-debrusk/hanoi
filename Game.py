


class Hanoi:
	def __init__(self, rings):
		self.numRings = rings
		self.towers = 3
		self.rings = []

		self.tower1 = []
		self.tower2 = []
		self.tower3 = []

		for x in range(self.numRings-1, -1, -1):
			self.rings.append(x + 1)

		for x in range(self.numRings):
			self.tower1.append(self.rings[x])


	def print_board(self):
		for x in range(self.numRings):
			print("   |      |      |   ")
			print("   " + str(self.tower1.pop()));
		print("   |      |      |   ")
		print("_____________________")

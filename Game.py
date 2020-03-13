


class Hanoi:
	def __init__(self, rings):
		self.numRings = rings
		self.towers = []
		for x in range(3):
			self.towers.append([])


		for x in range(self.numRings):
			self.towers[0].append(x + 1)
			self.towers[1].append(0)
			self.towers[2].append(0)


	def print_board(self):
		#self.make_move()
		#self.make_move()
		# for x in range(self.numRings):
		# 	print("   |      |      |   ")
		# 	print("   " + display(self.towers[0][x]) + "      " + display(self.towers[1][x]) + "      " + display(self.towers[2][x]) + "   ");
		# print("   |      |      |   ")
		# print("_____________________")
		print(self.towers)
		#print(self.get_top_ring_index(self.tower1))

	def get_top_ring_index(self, tower):
		index = 0
		for x in range(self.numRings):
			if (tower[x] != 0):
				index = x
				break
		return index

	def make_move(self):
		sourceIndex = self.get_top_ring_index(self.tower1)
		destinationIndex = self.get_top_ring_index(self.tower2) - 1
		self.tower2[destinationIndex] = self.tower1[sourceIndex]
		self.tower1[sourceIndex] = 0


def display(num):
	if (num == 0):
		return "|"
	else:
		return str(num)

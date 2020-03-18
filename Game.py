
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
		#self.make_move(0,1)
		for x in range(self.numRings):
			print("   |      |      |   ")
			print("   " + display(self.towers[0][x]) + "      " + display(self.towers[1][x]) + "      " + display(self.towers[2][x]) + "   ");
		print("   |      |      |   ")
		print("_____________________")
		#print(self.towers)

	def get_top_ring_index(self, tower):
		index = 0
		for x in range(self.numRings):
			if (self.towers[tower][x] != 0):
				index = x
				break
		return index

	def make_move(self, source, destination):
		if (source <= 2 and destination <= 2):
			sourceIndex = self.get_top_ring_index(source)
			destinationIndex = self.get_top_ring_index(destination) - 1
			destVal = self.towers[destination][destinationIndex + 1]
			sourceVal = self.towers[source][sourceIndex]
			if (sourceVal >  (destVal if destVal != 0 else 100) or sourceVal == 0 or source == destination):
				return False
			else:
				self.towers[destination][destinationIndex] = sourceVal
				self.towers[source][sourceIndex] = 0
				return True
		else:
			return False

	def check_victory(self):
		for x in range(self.numRings):
			if (self.towers[0][x] == 0 and self.towers[1][x] == 0):
				continue
			else:
				return False
		return True


def display(num):
	if (num == 0):
		return "|"
	else:
		return str(num)

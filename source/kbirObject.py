

class KeyboardRepresentation:
	def __init__(self, name, cols, rows):
		self.name    = name
		self.numColumns = cols
		self.numRows    = rows
		self.keyMatrix = [][]

	def addKey(key, row):
		keyMatrix[row].append(key)

	def __str__(self):
		return "Layout: " + self.name + "\n" + self.numColumns + " x " + self.numRows
	

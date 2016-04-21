

class KeyboardRepresentation:
	def __init__(self, name, cols, rows):
		self.name       = name
		self.numColumns = cols
		self.numRows    = rows
		self.layout     = []

	def addKey(self, key, layer, row):
		layout[layer][row].append(key)

	def printLayout(self):
		for layer in layout:
			print "Layer: "
			for row in layer:
				for column in row:
					print column + " "
				print "\n"


	def __str__(self):
		return "Layout: " + self.name + "\n" + self.numColumns + " x " + self.numRows
	

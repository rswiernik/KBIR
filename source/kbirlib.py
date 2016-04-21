

class KeyboardRepresentation:
	def __init__(self, name=None, cols=None, rows=None):
		if name is None:
			name = ""
		if cols is None:
			cols = 0
		if rows is None:
			rows = 0

		self.name	   = name
		self.numColumns = cols
		self.numRows	= rows
		self.layout	 = []
		self.global_settings = {}
		self.functions  = {}

	def setName(self, name):
		self.name = name

	def setNumCol(self, numColumns):
		self.numColumns = numColumns

	def setNumRows(self, numRows):
		self.numRows = numRows

	def addRow(self, rowData, layer):
		self.layout.append(rowData)

	def printLayout(self):
		for layer in self.layout:
			print "Layer: "
			for row in layer:
				for column in row:
					print column + " "
				print "\n"


	def __str__(self):
		return "Layout: " + self.name + "\n" + self.numColumns + " x " + self.numRows
	

from string import Template

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
		self.layout	 = {}
		self.globalSettings = {}
		self.functions  = {}

	def setName(self, name):
		self.name = name

	def setNumCol(self, numColumns):
		self.numColumns = numColumns

	def setNumRows(self, numRows):
		self.numRows = numRows

	def setGlobals(self, globalSettings):
		self.globalSettings = globalSettings

	def setFunctions(self, functions):
		self.functions = functions

	def addLayer(self, layer):
		self.layout[layer] = []

	def addRow(self, rowData, layer):
		self.layout[layer].append(rowData)

	def printLayout(self):
		for key in self.layout:
			print "Layer ", (key), ": "
			for row in self.layout[key]:
				print row
			print ""

	def generateLayout(self, firmwareName):
		if firmwareName is "tmk":
			return self.generateTMKLayout()

	def generateTMKLayout(self):
		fileLines = []
		with open("source/keyboardProfiles/tmk/layout.template", "r") as f:
			for line in f:
				fileLines.append(line)

		newLayoutString = ""
		for line in fileLines:
			newLayoutString = newLayoutString + line.strip() + "\n"

		layoutTemplate = Template(newLayoutString)

		layerTemplate = Template('''\
		[${layerNumber}] = KEYMAP_GRID( /* ${comment} */
		${layerData}\
		'''.strip())

		functionTemplate = Template('''\
		[${functionNum}] = ${functionValue}, /* ${comment} */\
		'''.strip())


		layers = []
		for layerNum in self.layout:
			layer = ""
			layerTemplateDict = dict(layerNumber=layerNum)
			for row in self.layout[layerNum][:-1]:
				layer = layer + "\t"
				for keyChar in row[:-1]:
					layer = layer + keyChar + ", "
				layer = layer + row[-1] + ",\n"
			finalRow = (self.layout[layerNum])[-1]
			layer = layer + "\t"
			for keyChar in finalRow[:-1]:
				layer = layer + keyChar + ", "
			layer = layer + finalRow[-1] + "),\n"
			layerTemplateDict["layerData"] = layer
			layerTemplateDict["comment"] = "This is a comment"
			layers.append(layerTemplate.safe_substitute(layerTemplateDict))

		layerString = ""
		for layer in layers:
			layerString = layerString + layer + "\n"


		functions = []
		functionNumber = 0
		for function in self.functions:
			functionDict = dict( comment=function, functionValue=self.functions[function], functionNum=functionNumber)
			functions.append(functionTemplate.safe_substitute(functionDict))
			functionNumber = functionNumber + 1

		functionString = ""
		for function in functions:
			functionString = functionString + function + "\n"


		layoutTemplateDict = dict(layers=layerString, functions=functionString)
		print layoutTemplateDict
		outputString = layoutTemplate.substitute(layoutTemplateDict)

		return outputString


	def __str__(self):
		return "Layout: " + self.name + "\n" + self.numColumns + " x " + self.numRows

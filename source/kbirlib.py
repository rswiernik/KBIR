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
		printedLayout = ""
		outputString = '''\		
		#include "keymap_common.h"

		/*
		 * This layout file is generated by KBIR - http://github.com/rswiernik/kbir
		 */
		const uint8_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

		{% layers %}

		};
		const uint16_t PROGMEM fn_actions[] = {

			{% fn_actions %}

		};\
		'''
		print outputString
		return outputString


	def __str__(self):
		return "Layout: " + self.name + "\n" + self.numColumns + " x " + self.numRows

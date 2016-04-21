import os
import sys
import argparse
import time
import logging

import kbirlib


def main(args):
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('-v', '--verbose', help='enable verbose output', action='store_true')
	parser.add_argument('-k', '--keyboard', action='store', dest='kbl_file', type=str, help='The file path to the kbl file you would like to use.')
	parser.add_argument('-o', '--output-file', action='store', dest='outputFilename', type=str, default='output.layout', help='Layout output filename')
	parser.add_argument('-f', '--firmware', action='store', dest='firmwareName', type=str, default='tmk', help='Fireware layout style to output to file')
	args = parser.parse_args()

	LOG_FORMAT = '%(asctime)-15s %(message)s'
	LOG_DATE = '%m/%d/%Y %H:%M:%S %Z  '
	LOG_LVL = logging.INFO
	if args.verbose:
		LOG_LVL = logging.DEBUG
	logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE, level=LOG_LVL)
	logging.debug('Verbose output enabled')


	logging.debug("Starting - %s: %s" % ("Building layout", args.kbl_file))
	
	layoutRepr = parseLayoutFile(args.kbl_file)
	generateFirmwareLayout(args.outputFilename, args.firmwareName, layoutRepr)

	logging.debug("Stopping - %s: %s" % ("Ending layout build", args.kbl_file)) 



def generateFirmwareLayout(outputFilename, firmwareName, kbirObj):
	if os.path.isfile(outputFilename):
		logging.error("Error when writing file: File %s exists" % (outputFilename))
		exit(1)
	else:
		layoutOutput = kbirObj.generateLayout(firmwareName)
		with open(outputFilename, "w") as f:
			if layoutOutput != "firmware not found":
				f.write(layoutOutput)
			else:
				logging.error("Error: firmware \'%s\' is not supported" % (firmwareName))
				exit(1)


def parseLayoutFile(filename):
	logging.debug("Parsing file: %s" % (filename))
	
	lines = []
	with open(filename, "r") as f:
		for line in f:
			lines.append(line)
	
	global_settings = {}
	function_settings = {}
	kbirObj = kbirlib.KeyboardRepresentation()
	currentLine = 0
	while currentLine < len(lines):
		line = (lines[currentLine].strip()).rstrip()
		logging.debug("analyzing line -> %s" % (line))
		if line == "---":
			while True:
				if currentLine < (len(lines) - 1):
					currentLine = currentLine + 1
					line = lines[currentLine].strip()
					logging.debug("title lines -> \'%s\'" % (line))
					if ":" in line:
						setting = line.split(':')
						logging.debug("def global -> \'%s\'" % (setting))
						global_settings[setting[0]] = setting[1].strip()
				if currentLine >= (len(lines)-1) or line == "---":
					break
		if line == "-- functions --":
			while True:
				if currentLine < (len(lines) - 1):
					currentLine = currentLine + 1
					line = lines[currentLine].strip()
					logging.debug("function lines -> \'%s\'" % (line))
					if line == "":
						continue
					if ":" in line:
						function = line.split(':')
						logging.debug("def func -> \'%s\'" % (function))
						function_settings[function[0]] = function[1].strip()
				if currentLine >= (len(lines)-1) or line == "---":
					break
		if line == "-- layers --":
			currentLayer = -1
			while True:
				if currentLine < (len(lines) - 1):
					currentLine = currentLine + 1
					line = lines[currentLine].strip()
					logging.debug("layer %s lines -> \'%s\'" % (currentLayer, line))
					if line == "":
						currentLayer = currentLayer + 1
						kbirObj.addLayer(currentLayer)
						continue
					layerRow = line.split()
					row = []
					for key in layerRow:
						row.append(key)
					logging.debug("def row -> \'%s\'" % (row))
					kbirObj.addRow(row, currentLayer)
				if currentLine >= (len(lines)-1) or line == "-- layers --":
					break
		logging.debug("def row -> \'%s\'" % (kbirObj.printLayout()))
		currentLine = currentLine + 1
	
	kbirObj.setGlobals(global_settings)
	kbirObj.setFunctions(function_settings)
	return kbirObj

if __name__ == '__main__':
	sys.exit(main(sys.argv))

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
	args = parser.parse_args()

	LOG_FORMAT = '%(asctime)-15s %(message)s'
	LOG_DATE = '%m/%d/%Y %H:%M:%S %Z  '
	LOG_LVL = logging.INFO
	if args.verbose:
		LOG_LVL = logging.DEBUG
	logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE, level=LOG_LVL)
	logging.debug('Verbose output enabled')


	logging.debug("Starting - %s: %s" % ("Building layout", args.kbl_file))
	
	parseLayoutFile(args.kbl_file)

	logging.debug("Stopping - %s: %s" % ("Ending layout build", args.kbl_file)) 


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
	



if __name__ == '__main__':
	sys.exit(main(sys.argv))

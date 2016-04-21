import os
import sys
import argparse
import time
import logging

import kbirlib


def main(args):
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('-v', '--verbose', help='enable verbose output', action='store_true')
	parser.add_argument('-k', '--keyboard', action='store', dest='keyboard_type', type=str, help='keyboard type')
	args = parser.parse_args()

	LOG_FORMAT = '%(asctime)-15s %(message)s'
	LOG_DATE = '%m/%d/%Y %H:%M:%S %Z  '
	LOG_LVL = logging.INFO
	if args.verbose:
		LOG_LVL = logging.DEBUG
	logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE, level=LOG_LVL)
	logging.debug('Verbose output enabled')


	logging.debug("Starting - %s: %s" % ("Building layout", args.keyboard_type))

	logging.debug("Stopping - %s: %s" % ("Ending layout build", args.keyboard_type)) 


def parseLayoutFile(filename):
	logging.debug("Parsing file: %s" & (filename))

	with open(filename, "r") as f:
		for line in f:
			print line



if __name__ == '__main__':
	sys.exit(main(sys.argv))

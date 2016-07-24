#!/bin/bash

if [[ $# -ne 0 ]]; then
	echo "Running test builds without args..."
	exit 0
fi

OUTPUT_FILE="output.layout"

if [[ -e ${OUTPUT_FILE} ]]; then
	read -p "File ${OUTPUT_FILE} exists. Would you like to delete it? [Y/n]" -n 1 -r
	echo
	if [[ $REPLY =~ ^[Yy]$ ]]; then
		echo "rm ${OUTPUT_FILE}"
		rm "${OUTPUT_FILE}"
	else
		echo "Leaving file, build might fail."
	fi
fi

echo "Alright, let's do this... LEEROY"

python source/kbirparse.py -k layouts/planck_standard.kbl -v

cat output.layout

if [[ $? -eq 0 ]]; then
	echo "Build successful."
	exit 0
else
	echo "Build failed..."
	exit 1
fi

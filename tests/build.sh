#!/bin/bash

if [[ $# -ne 0 ]]; then
	echo "Running test builds without args..."
	exit 0
fi

echo "Alright, let's do this... LEEROY"

python source/kbirparse.py -k layouts/planck_standard.kbl


exit 0

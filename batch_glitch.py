#!/bin/python3 

import os, argparse
import random
from os.path import basename

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-i", "--input", help="input folder")
parser.add_argument('-c', action='store', dest='codec',help='codec', default="libxvid")

args = parser.parse_args()

folderin = args.input
codec = args.codec

# create dir for encoded files

for filename in os.listdir(folderin):
	if os.path.isdir(filename):
		continue
	os.system("python tomato.py -i " + folderin +  "/" +  filename + " -m pulse -c 5 -n 1")
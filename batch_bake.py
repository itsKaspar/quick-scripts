#!/bin/python3 

import os, argparse
import random
from os.path import basename

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-i", "--input", help="input folder")

args = parser.parse_args()

folderin = args.input

# create dir for encoded files

if not os.path.exists(folderin + "-baked"):
	os.makedirs(folderin + "-baked")

for filename in os.listdir(folderin):
	if os.path.isdir(filename):
		continue
	os.system("ffmpeg -i " + folderin +  "/" +  filename + " -c:v libx264 -crf 0 " + folderin + "-baked/" + os.path.splitext(filename)[0] + ".mp4")
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

if not os.path.exists(folderin + "-enc"):
	os.makedirs(folderin + "-enc")

for filename in os.listdir(folderin):
	if os.path.isdir(filename):
		continue
	os.system("ffmpeg -i " + folderin +  "/" +  filename + " -c:v " + codec + " -bf 0 -an -qscale:v 1 -g 9999999 " + folderin + "-enc/" + os.path.splitext(filename)[0] + ".avi")
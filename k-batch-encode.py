import os, argparse
from os.path import basename
import random

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-i", "--input", help="input folder")

args = parser.parse_args()

folderin = args.input
folderout = "enc-" + folderin

containers = (".mp4",".avi",".mkv",".mov")

if not os.path.exists(folderin + "/" + folderout): 
	os.makedirs(folderin + "/" + folderout)

for filename in os.listdir(folderin):
	if os.path.splitext(filename)[1] in containers:
		os.system("ffmpeg -i " + folderin + "/" + filename + " -c:v libxvid -qscale:v 5 " + folderin + "/" + folderout + "/enc-" + os.path.splitext(filename)[0] + ".mp4")


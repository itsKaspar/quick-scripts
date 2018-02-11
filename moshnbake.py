#!/bin/python3 
import os
from os.path import basename


for filename in os.listdir("."):
	os.system("ffmpeg -i " + filename + " -c:v libxvid -qscale:v 1 -an -bf 0 -g 900 ENC" + os.path.splitext(filename)[0] + ".avi")
for filename in os.listdir("."):
	if "ENC" in filename:
		os.system("python tomato.py -i " + filename + " -m pulse -c 15 -n 1 OUT" + os.path.splitext(filename)[0] + ".avi")
for filename in os.listdir("."):
	if "OUT" in filename:
		os.system("mencoder " + filename + " -o OUT2" + os.path.splitext(filename)[0] + ".mov -ovc x264")
for filename in os.listdir("."):
	if "OUT2" in filename:
		os.system("ffmpeg -i " + filename + " -c:v prores_ks BAKED" + os.path.splitext(filename)[0] + ".mov")

#!/bin/python3 
import os
from os.path import basename

for filename in os.listdir("."):
	if "OUT" in filename:
		os.system("mencoder " + filename + " -o OUT2" + os.path.splitext(filename)[0] + ".mov -ovc x264")

for filename in os.listdir("."):
	if "OUT2" in filename:
		os.system("ffmpeg -i " + filename + " -c:v prores_ks BAKED" + os.path.splitext(filename)[0] + ".mov")

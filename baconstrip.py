#!/bin/python3 
import os
from os.path import basename

if not os.path.exists("baked"):
	os.makedirs("baked")

if not os.path.exists("temp"):
	os.makedirs("temp")

for filename in os.listdir("."):
	if os.path.isdir(filename):
		continue
	os.system("mencoder " + filename + " -o temp/" + os.path.splitext(filename)[0] + ".mov -ovc x264 -oac lavc")

for filename in os.listdir("temp"):
	if os.path.isdir(filename):
		continue
	os.system("ffmpeg -i temp/" + filename + " -c:v libx264 -crf 0 -preset ultrafast baked/" + os.path.splitext(filename)[0] + ".mov")

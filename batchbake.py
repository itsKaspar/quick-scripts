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
	os.system("mencoder " + filename + " -nosound -o temp/" + os.path.splitext(filename)[0] + ".mov -ovc x264")

for filename in os.listdir("temp"):
	if os.path.isdir(filename):
		continue
	os.system("ffmpeg -i temp/" + filename + " -c:v prores_ks baked/" + os.path.splitext(filename)[0] + ".mov")

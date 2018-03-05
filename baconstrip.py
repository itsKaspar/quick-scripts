#!/bin/python3 
import os
from os.path import basename

if not os.path.exists("bacon"):
	os.makedirs("bacon")

for filename in os.listdir("."):
	if os.path.isdir(filename):
		continue
	os.system("ffmpeg -i " + filename + " -c:v libxvid -crf 0 -preset ultrafast -c:a libmp3lame encoded/" + os.path.splitext(filename)[0] + ".mkv")

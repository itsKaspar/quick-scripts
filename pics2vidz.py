#!/bin/python3 
import os
from os.path import basename

if not os.path.exists("vidz"):
	os.makedirs("vidz")


for filename in os.listdir("."):
	if os.path.isdir(filename):
		continue
	os.system("ffmpeg -loop 1 -i " + filename + " -t 0.5 -vf scale=1080:648 -c:v libx264 vidz/" + os.path.splitext(filename)[0] + ".mp4")

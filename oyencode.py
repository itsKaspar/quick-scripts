#!/usr/bin/python2.7

import os
from os.path import basename

d = "encoded" 	# directory name
enc = "libx264"	# encoder
ext = ".mp4"	# extension
enc_opt = ""	# encoder options

## if it is a webvideo and needs to be played by user on browser before it finished downloading
# -movflags +faststart
## tuning options // other options : animation
# -tune film

if not os.path.exists(d): 
	os.makedirs(d)

	for filename in os.listdir("."):
		if os.path.isdir(f):
	      		continue
			
		fnoext = os.path.splitext(f)[0]
		output = d + "/" + fnoext + ext
		os.system("ffmpeg -i " + f + " -c:v " + enc + " " + enc_opt + " " + output)

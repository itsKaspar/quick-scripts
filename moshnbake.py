#!/bin/python3 
from time import sleep
import os

i = 1

for filename in os.listdir("."):
	stri = str(i) 
	os.system("ffmpeg -i " + filename + " -c libxvid -qscale:v 1 -an -bf 0 -g 400 bad1" + stri + ".avi")
	os.system("python tomato.py -i bad1" + stri + ".avi -m pulse -c 2 -n 1 bad2" + stri + ".avi" )
	#os.system("mencoder -forceidx -oac copy -ovc copy badB" + stri + ".avi -o bad2" + stri + ".avi")
	os.system("mencoder bad2" + stri + ".avi -o bad3" + stri + ".mov -ovc x264")
	os.system("ffmpeg -i bad3" + stri + ".mov -c:v prores_ks final" + stri + ".mov")
	os.system("del bad*")
	i = i + 1

#!/bin/python3  

from time import sleep
import os
i = 1

while i < 33 :
	os.system("ffmpeg -ss 0 -i " + stri + ".mov -c copy -an -t 3 3s" + stri + ".mov")
	sleep(1)
	os.system("ffmpeg -i 3s" + stri + ".mov -vf reverse rev" + stri + ".mov")
	sleep(1)
	os.system("ffmpeg -i \"concat:3s" + stri + ".mov|" + stri + ".mov -c copy scripted" + stri + ".mov")
	sleep(1)
	os.system("del 3s" + stri + ".mov")
	sleep(1)
	os.system("del rev" + stri + ".mov")
	sleep(1)

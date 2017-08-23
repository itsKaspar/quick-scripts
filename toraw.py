#!/bin/python3  

from time import sleep
import os
i = 1

while i < 90 :
	stri = str(i)
	os.system("ffmpeg -i " + stri + ".avi -c:v rawvideo -pix_fmt yuv420p out" + stri + ".yuv")
	i = i + 1
	sleep(1)
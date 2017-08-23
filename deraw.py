#!/bin/python3  

from time import sleep
import os
i = 1

while i < 90 :
	stri = str(i)
	os.system("ffmpeg -f rawvideo -pix_fmt yuv420p -s 4096x2178 -r 25 g" + stri + ".yuv " + stri + ".mov")
	i = i + 1
	sleep(1)
#!/bin/python3  

from time import sleep
import os

j = 1
i = 0

while i < 1343 :
	stri = str(i)
	strj = str(j)
	os.system("ffmpeg -ss " + stri +  " -i chimere.mov -c copy -an -t 15 " + strj + ".avi")
	i = i + 15
	j = j + 1
	sleep(1)
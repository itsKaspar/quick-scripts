#!/bin/python3  

from time import sleep
import os

j = 1
i = 0

#make one inputs, cut every, + detect how long the video is
while i < 5500 :
	stri = str(i)
	strj = str(j)
	os.system("ffmpeg -ss " + stri +  " -i video.mp4 -t 900 -c:v libx264 " + strj + ".mp4")
	i = i + 900
	j = j + 1
	sleep(2)

#!/bin/python3 
import os
import random
 
i = 0
j = 1

while i < 1519 : #length in seconds of movie
	k = random.randint(2, 8) #select random lengths for cuts
	stri = str(i)
	strj = str(j)
	strk = str(k)		
	
	os.system("ffmpeg -ss " + stri +  " -t " + strk + " -i montage4K.mov -f rawvideo -pix_fmt yuv420p - |\
	ffmpeg -f alaw -ar 48000 -ac 1 -i - -af atempo=0.9999999999901,asetrate=48000 -f alaw -ar 48000 -ac 1 - |\
	ffmpeg -f rawvideo -vcodec rawvideo -s 4096x2160 -r 25 -pix_fmt yuv420p -i - -c:v libx264 -preset ultrafast -qp 0 " + strj + ".avi ")
	i = i + k
	j = j + 1

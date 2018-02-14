#!/usr/bin/python2.7

import os
import random
from moviepy.editor import VideoFileClip
import re

g = 600 # nb of seconds that we strip from beginning and end of movie to avoid credits
j = 5 # nb of cuts you want
i = 0




if not os.path.exists("results"): 
	os.makedirs("results")

while i < j :
	for filename in os.listdir("."):
		if os.path.isdir(filename) or filename == "sonia.py":
	      		continue
			
		clip = VideoFileClip(filename)
		film_duration = clip.duration
		
		min = g
		max = int(film_duration) - g - 180
		
  		k = random.randint(min, max)
		os.system("ffmpeg -ss " + str(k) +  " -i " + filename + " -t 10 -c:v libx264 results/" + str(i) + ".mp4")
		
		print "################################################"
		print "made cut from " + str(k) + "sec to " + str(k + 180) + "sec " 
		print "################################################"
		
		i += 1
	

  
  


	

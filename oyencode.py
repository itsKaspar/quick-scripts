#!/usr/bin/python2.7

import os

if not os.path.exists("encoded"): 
	os.makedirs("encoded")

	for filename in os.listdir("."):
		if os.path.isdir(filename) or filename == "sonia.py":
	      		continue
			
		clip = VideoFileClip(filename)
		film_duration = clip.duration
		
		min = g
		max = int(film_duration) - g - t
		
  		k = random.randint(min, max)
		os.system("ffmpeg -ss " + str(k) +  " -i " + filename + " -t " + str(t) + " -c:v libx264 results/" + str(i) + ".mp4")
		
		i += 1

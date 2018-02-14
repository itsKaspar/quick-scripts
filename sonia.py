#!/bin/python3  

import os
import random
import subprocess
import re

g = 600 # nb of seconds that we strip from beginning and end of movie to avoid credits
j = 5 # nb of times you wanna go through each movie and cut shit

if not os.path.exists("results"): 
	os.makedirs("results")

while i < j :
	for filename in os.listdir("."):
		if os.path.isdir(filename):
	      		continue
			
		process = subprocess.Popen(['/usr/bin/ffmpeg',  '-i', filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    		stdout, stderr = process.communicate()
    		matches = re.search(r"Duration:\s{1}(?P\d+?):(?P\d+?):(?P\d+\.\d+?),", stdout, re.DOTALL).groupdict()
   		film_duration = matches['minutes']
		
  		k = random.randint(g, film_duration-g-180)
		os.system("ffmpeg -ss " + k +  " -i " + filename + " -t 180 -c:v libx264 results/" + os.path.splitext(filename)[0] + ".mp4")

	i++




  
  


	

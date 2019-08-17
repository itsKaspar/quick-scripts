import os, argparse
import random
from moviepy.editor import VideoFileClip

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-i", "--input", help="input file")
parser.add_argument('-d', action='store', dest='duration',help='duration', default=0)
parser.add_argument("output", help="output file")

args = parser.parse_args()

filein = args.input
fileout = args.output
d = int(args.duration)

clip = VideoFileClip(filein)
i = 0
j = 0
temp = str(random.randint(1000000,10000000))

#reverse and delete first frame for more fluid boomerang
os.system("ffmpeg -i " + filein + " -vf select=\"gte(n\, 1)\",reverse " + temp + "-rev.mp4")
f= open(temp + "-concat.txt","w+")

#if duration is not given then just a simple boomerang
if d == 0:
	f.write("file '" + filein + "'\n")
	f.write("file '" + temp + "-rev.mp4'\n")
	f.close()
	os.system("ffmpeg -f concat -safe 0 -i " + temp + "-concat.txt -c copy " + fileout)

#if duration is given then boomerang until end of duration
else:
	while i < d :

		if j % 2 == 0:
			f.write("file '" + filein + "'\n")
		else:
			f.write("file '" + temp + "-rev.mp4'\n")	

		i = i + int(clip.duration)
		j = j + 1
	f.close()
	os.system("ffmpeg -f concat -safe 0 -i " + temp + "-concat.txt -c copy -t " + str(d) + " " + fileout)

	
os.remove(temp + "-rev.mp4") 
os.remove(temp + "-concat.txt") 




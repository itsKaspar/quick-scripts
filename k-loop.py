import os, argparse
import random
from moviepy.editor import VideoFileClip

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-i", "--input", help="input file")
parser.add_argument('-d', action='store', dest='duration',help='duration', default=0)
parser.add_argument('-m', action='store', dest='mode',help='mode', default="boomerang")
parser.add_argument('-c', action='store', dest='crossfade',help='crossfade', default=1)
parser.add_argument("output", help="output file")

args = parser.parse_args()

filein = args.input
fileout = args.output
mode = args.mode
d = int(args.duration)
c = int(args.crossfade)
clip = VideoFileClip(filein)
temp = str(random.randint(1000000,10000000))

#
# MODE : BOOMERANG
# #################

if mode == "boomerang":

	i = 0
	j = 0

	os.system("ffmpeg -i " + filein + " -vf select=\"gte(n\, 1)\",reverse " + temp + "-rev.mp4")
	f= open(temp + "-concat.txt","w+")

	if d == 0:
		f.write("file '" + filein + "'\n")
		f.write("file '" + temp + "-rev.mp4'\n")
		f.close()
		os.system("ffmpeg -f concat -safe 0 -i " + temp + "-concat.txt -c copy " + fileout)

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

#
# MODE : CROSSFADE
# #################

elif mode == "crossfade":

	i = 0
	j = 0

# when the fade duration is more than half the video duration
# it isn't possible to fade.
# so make it half
	if c > (int(clip.duration)/2):
		c = int(clip.duration)/2

	if d != 0: #quick fix for file name and right output

		fileout2 = fileout
		fileout = temp + ".mp4"

	os.system("ffmpeg -i "+ filein +" -filter_complex \"[0]split[v1][v2];\
		[v2]trim=duration=" + str(c) + ",fade=d=" + str(c) + ":alpha=1,\
    	setpts='PTS+(max(" + str(clip.duration) + "-2*" + str(c) + ",0)/TB)'[faded];\
		[v1]trim=" + str(c) + ",setpts=PTS-STARTPTS[main];\
		[main][faded]overlay\"\
		-vcodec libx264 -an -preset veryslow -movflags faststart " + fileout + "")

	if d != 0:

		f= open(temp + "-concat.txt","w+")
		clip2 = VideoFileClip(fileout)
		while i < d :

			f.write("file '" + fileout + "'\n")	

			i = i + int(clip2.duration)

		f.close()
		os.system("ffmpeg -f concat -safe 0 -i " + temp + "-concat.txt -c copy -t " + str(d) + " " + fileout2)

	if d != 0:
		os.remove(temp + ".mp4")
		os.remove(temp + "-concat.txt") 



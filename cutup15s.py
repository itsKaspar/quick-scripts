import os, argparse
from moviepy.editor import VideoFileClip

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-i", "--input", help="input file")
args = parser.parse_args()
filein = args.input

clip = VideoFileClip(filein)
i = 1
j = 0
n = 10

while i < clip.duration :
	os.system("ffmpeg -ss " + str(i) +  " -i " + filein +  " -t " + str(n) + "  -c:v libx264 " + str(j) + ".mp4")
	i = i + n
	j = j + 1

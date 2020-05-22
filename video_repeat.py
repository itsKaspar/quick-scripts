import os, argparse
import random
from moviepy.editor import VideoFileClip

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-i", "--input", help="input file")
parser.add_argument('-n', action='store', dest='ntimes',help='duration', default=3)
parser.add_argument("output", help="output file")

args = parser.parse_args()

filein = args.input
fileout = args.output
n = int(args.ntimes)
clip = VideoFileClip(filein)
temp = str(random.randint(1000000,10000000))

# Actual Program

i = 0

f= open(temp + "-concat.txt","w+")

for i in range(n):
    f.write("file '" + filein + "'\n")

f.close()

os.system("ffmpeg -f concat -safe 0 -i " + temp + "-concat.txt -c copy " + fileout)
	
os.remove(temp + "-concat.txt") 
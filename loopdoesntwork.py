import os, argparse
from moviepy.editor import VideoFileClip

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-i", "--input", help="input file")
args = parser.parse_args()
filein = args.input

clip = VideoFileClip(filein)

os.system('ffmpeg -i "concat:' + filein + '|' + filein + '|' + filein + '" -c:v libxvid -an -bf 0 -qscale:v 1 -g 999999 x3-' + filein)
os.system("python tomato.ty -i x3-" + filein + " -m ikill x3-NOI-" + filein)
os.system("ffmpeg -i x3-NOI-" + filein + " -c:v libx264 -crf 0 x3-NOI-baked-" + filein)
os.system("ffmpeg -i x3-NOI-baked-" + filein + " -ss " + str(clip.duration) + " -t " + str(clip.duration) + " Gloop-" + filein)


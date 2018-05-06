#!/usr/bin/python2.7

import argparse, os
from PIL import Image


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-i", "--img", help="input img", dest='image')
parser.add_argument("-v", "--vid", help="input video", dest='video' )
parser.add_argument("file", help="output file")

args = parser.parse_args()

img = args.image
vid = args.video
fileout = args.file

im=Image.open(img)
print(im.size[0])
print(im.size[1])

os.system("ffmpeg -loop 1 -y -i "+ img +" -t 1 -r 29,97 -c:v libx264 image.avi")
os.system('ffmpeg -i ' + vid + ' -vf format=gray,scale=' + str(im.size[0]) + 'x' + str(im.size[1]) + ' -c:v libx264 video.avi ')
os.system('ffmpeg -i "concat:image.avi|video.avi" -c libxvid -an -bf 0 -g 999 -qscale:v 1 ready.avi')
os.system('python2 tomato.py -i ready.avi -m ikill ikilled.avi')
os.system('python2 tomato.py -i ikilled.avi -m pulse -c 15 -n 1 ' + fileout + '')

#os.system('del image.avi')
#os.system('del video.avi')
#os.system('del ready.avi')
#os.system('del ikilled.avi')

#!/usr/bin/env python3
import os, glob
from PIL import Image

#Run script with the folder path where the files to convert are as an argument.
input = sys.argv[1]
output = "/opt/icons/"

im_size = (128, 128) #Output image size in px
im_rot = 270 #Rotation degrees (Counter clocl-wise)
im_format = "JPEG"

for file in glob.glob(input, "ic_*"): #Iterate over all files starting with "ic_"
        im = Image.open(file).convert("RGB") #Open file as image and convert to RGB
        im.resize(im_size).rotate(im_rot).save(output + file, "JPEG") #Resize, rotate and save as JPEG

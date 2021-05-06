#!/usr/bin/env python3

from PIL import Image
import os
import re

permissions = 0o777 #the 0o prefix is for the octal numbering system

image_path = r".\images"
project_path = r"."

#if the output folder doesn't already exist, create it
if not os.path.exists(project_path+r"\output"):
    os.mkdir(project_path+r"\output",permissions)

#rotate and resize images
for i, image in enumerate(os.listdir(image_path)):
    #only handles images in .tiff or .jpg format
    if re.search(r'.+(.{5})$',image).groups()[0] == '.tiff' or re.search(r'.+(.{4})$',image).groups()[0] == '.jpg':
        im = Image.open(image_path+"\\"+image)
        if re.search(r'.+(.{5})$',image).groups()[0] == '.tiff':
            im = im.convert('RGB') #.tiff is RGBA, and JPG only support RGB
        im.rotate(270).resize((128,128)).save(project_path+"\output\\"+"flipped_and_resized_{}.jpg".format(image))

    
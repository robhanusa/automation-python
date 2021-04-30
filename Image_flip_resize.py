# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 06:08:08 2021

@author: rkhan
"""

from PIL import Image
import os

permissions = 0o777 #the 0o prefix is for the octal numbering system

image_path = r"C:\Users\rkhan\pythontest\courserafinalproject\images"
project_path = r"C:\Users\rkhan\pythontest\courserafinalproject"

#if the output folder doesn't already exist, create it
if not os.path.exists(project_path+r"\output"):
    os.mkdir(project_path+r"\output",permissions)

#rotate and resize images
for i, image in enumerate(os.listdir(image_path)):
    im = Image.open(image_path+"\\"+image)
    im.rotate(270).resize((128,128)).save(project_path+"\output\\"+"flipped_and_resized{}.jpg".format(i))
    
#I could improve this by making it a function with input of file path
#!/usr/bin/env python3

r'''
from PIL import Image
import os
import re

image_path = r"C:\Users\rkhan\pythontest\courserafinalproject\automation-python\supplier-data\images"

pattern = r'(.+)(\.tiff)'
permissions = 0o777 
#rotate and resize images

for image in os.listdir(image_path):
    if not image == 'output':
        result = re.search(pattern,image)
        im = Image.open(image_path+"\\"+image)
        rgb_im = im.convert('RGB') #.tiff is RGBA, and JPG only support RGB
        rgb_im.resize((600,400)).save(image_path+"\output\\"+"{}.jpg".format(result.groups()[0]))

#below is the 2nd part:
import requests
from PIL import Image
import os
import re

image_path = r"supplier-data/images"

pattern = r'.+(\.tiff)'
url = "http://localhost/upload/"
for image in os.listdir(image_path):
    if not re.search(pattern,image) == None:
        with open("supplier-data/images/"+image,'rb') as opened:
            r = requests.post(url, files={'file': opened})
            
'''
#below is 3rd part, run.py:
import os
import requests
import json

file_path = r"C:\Users\rkhan\pythontest\courserafinalproject\automation-python\supplier-data\descriptions"

fruits_dict_list = []
for file in os.listdir(file_path):
    with open(file_path+'\\'+file, 'r') as f:
        fruits_dict = {}
        description_list = []
        for line in f:
            description_list.append(line)
        fruits_dict['name'] = description_list[0]
        weight_number = description_list[1].split( )
        fruits_dict['weight'] = weight_number[0]
        fruits_dict['description'] = description_list[2]
        #need to get image name below. I think that if file = 001.txt,
        #image name = 001.jpg, so I could make this simple
        fruits_dict['image_name'] = 
        fruits_dict_list.append(fruits_dict)
            

with open('fruits.json', 'w') as fruits_json:
    json.dump(fruits_dict_list, fruits_json)

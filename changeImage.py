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
            

#below is 3rd part, run.py:
import os
import requests
import json
import re

file_path = r"C:\Users\rkhan\pythontest\courserafinalproject\automation-python\supplier-data\descriptions"

fruits_dict_list = []
for file in os.listdir(file_path):
    with open(file_path+'\\'+file, 'r') as f:
        fruits_dict = {}
        description_list = []
        for line in f:
            description_list.append(line)
        fruits_dict['name'] = description_list[0].strip()
        weight_number = description_list[1].split( )
        fruits_dict['weight'] = int(weight_number[0])
        fruits_dict['description'] = description_list[2]
        #need to get image name below. I think that if file = 001.txt,
        #image name = 001.jpg, so I could make this simple
        fruits_dict['image_name'] = re.search(r'^(\d+)\.txt$',file).groups()[0]+'.jpg'
        fruits_dict_list.append(fruits_dict)
            

with open('fruits.json', 'w') as fruits_json:
    json.dump(fruits_dict_list, fruits_json)
    
#with open('fruits.json') as fruits_json:
#    r = requests.post(http://[linux-instance-external-IP]/fruits, json = fruits_json)


#below is the 4th part, reports.py
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime
import json

today = datetime.date.today()

report = SimpleDocTemplate(r"C:\Users\rkhan\pythontest\courserafinalproject\processed.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("Processed Update on {} <br/><br/>".format(today.strftime('%b %d, %Y')), styles["h1"])

with open('fruits.json', 'r') as fruits_json:
    fruits = json.load(fruits_json)
    
body_string = ""
for dict in fruits:
    body_string += "name: {} <br/>weight: {} lbs<br/><br/>".format(dict['name'],
                                                                   dict['weight'])

body =  Paragraph(body_string, styles["Normal"])

report.build([report_title, body])

#below is the 4.5th part, sending over email
from email.message import EmailMessage
import sys

def main(argv):
    message = EmailMessage()
    
    message['From'] = "automation@example.com"
    message['To'] = “<user>@example.com” #need to fill in user
    message['Subject'] = 'Upload Completed - Online Fruit Store'
    msg_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message.set_content(msg_body)
    attachment_path = "/tmp/processed.pdf"
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as ap:
      message.add_attachment(ap.read(),
      maintype=mime_type,
      subtype=mime_subtype,
      filename=os.path.basename(attachment_path))
    emails.send(message)
    
if __name__ == "__main__":
  main(sys.argv)
  
'''

#5th function, health_check.py
import psutil
import shutil
import socket

# checks if cpu usage is > 80%
cpu_percent = psutil.cpu_percent()

# check if Available disk space is lower than 20%
disk_space = shutil.disk_usage('/')[2]/shutil.disk_usage('/')[0]*100

#available memory in MB
memory_MB = psutil.virtual_memory().available//(1024**2)

#get local host
local_host = socket.gethostname()

def main(argv):
    message = EmailMessage()
    
    message['From'] = "automation@example.com"
    message['To'] = “<user>@example.com” #need to fill in user
        
    if cpu_percent > 80:
        message['Subject'] = 'Error - CPU usage is over 80%'
        msg_body = "Please check your system and resolve the issue as soon as possible."
        message.set_content(msg_body)
        emails.send(message)
        
    if disk_space < 20:
        message['Subject'] = 'Error - Available disk space is less than 20%'
        msg_body = "Please check your system and resolve the issue as soon as possible."
        message.set_content(msg_body)
        emails.send(message)  
        
    if memory_MB < 500:
        message['Subject'] = 'Error - Available memory is less than 500MB'
        msg_body = "Please check your system and resolve the issue as soon as possible."
        message.set_content(msg_body)
        emails.send(message)  
    
    if local_host == "127.0.0.1":
        message['Subject'] = 'Error - localhost cannot be resolved to 127.0.0.1'
        msg_body = "Please check your system and resolve the issue as soon as possible."
        message.set_content(msg_body)
        emails.send(message)  
        
if __name__ == "__main__":
  main(sys.argv)
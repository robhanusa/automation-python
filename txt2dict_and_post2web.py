# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import requests

#list all .txt files in folder using os.listdir()
file_path = r'C:\Users\rkhan\pythontest\courserafinalproject\reviews'
reviews = os.listdir(file_path)

#convert .txt file to dict keeping title, name, date, and feedback as keys
#the txt files are all formatted the same way with line breaks between fields
def txt2dict(file):
    with open(file_path+"\\"+file, 'r') as f:
        lines = f.readlines()
        dict = {'title': lines[0].strip(),
             'name': lines[1].strip(),
             'date': lines[2].strip(),
             'feedback': lines[3].strip()}
        return dict
        
#use request.post() to upload to company website. Note that for this code
#truely to work, an appropriate URL is needed.
def post2web(url):
    for review in reviews:
        review_dict = txt2dict(review)
        response = requests.post(url, data=review_dict)
        return response.status_code 
    
post2web() #need to add appropriate url argument
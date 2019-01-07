#!/bin/python3
import os
import sys
import urllib3
import requests
import shutil
import html
import array

#disables ssl warning
urllib3.disable_warnings()

#change directory
home = os.environ['HOME']
#folder = input('Name a folder: ')

#check if direcotry exists
# if os.path.exists(home+'/'+folder) == False:
#     os.mkdir(home+'/'+folder)
# os.chdir(home+'/'+folder)

#sets array variables
fileArr = []
linkArr = []
urlArr = []

#sets url to get data
url = input('URL containing PDF links: ')

urlArr = url.split('/')
#get site
site = urlArr[3]

#get data
response = requests.get(url,verify=False)
#print(response.text)
#sets htmlParser Params
from html.parser import HTMLParser
class dataParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            if attrs[0][1].endswith('pdf'):
                linkArr.append(attrs[0][1])
    #def handle_data(self, data):
    #    pdf = data.endswith('pdf')
    #    if pdf == True:
    #        print('File Found: '+data + '. Adding file to list.')
    #        fileArr.append(data)

#parses data
parser = dataParser()
parser.feed(response.text)
for item in linkArr:
    print(item)
    if item.startswith('htt'):
        print('full link')
    elif item.startswith('.'):
        print('relative to page')
    elif item.startswith('/'):
        print('url from site')

#checks if file exists.Downloads file if it doesn't
# for item in fileArr:
#     if os.path.exists(item):
#         print(item+' exists. Skipping file.')
#     else:
#         print('starting download of '+ item)
#         itemURL = site+'/'+item
#         def download_file(itemURL):
#             filename = item
#             r = requests.get(itemURL, stream=True)
#             with open(filename, 'wb') as f:
#                 shutil.copyfileobj(r.raw, f)
#             return filename
#         download_file(itemURL)

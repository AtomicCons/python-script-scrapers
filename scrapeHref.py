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
if url.startswith('http') == False:
    url = input('Please put the URL with the protocol.. hint. https:// or http://')

urlArr = url.split('/')

#get site
protocol = urlArr[0]
site = urlArr[2]


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
    iArr = item.split('/')
    filename = iArr[-1]
    if item.startswith('htt'):
        link = item
        print('filename: ' + filename + '   whole link  Link: '+ link)
    elif item.startswith('.'):
        link = url+item
        print('filename: ' + filename + ' starts with .  Link: '+ link)
    elif item.startswith('/'):
        link = protocol+site+item
        #link = link.replace('//','/')
        print('filename: '+filename + 'starts with /  Link: '+link)
    else:
        print(url+'/'+filename + ' not sure')


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

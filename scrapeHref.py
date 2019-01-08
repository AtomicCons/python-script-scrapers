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
folder = input('Name a folder: ')

#check if direcotry exists
if os.path.exists(home+'/'+folder) == False:
    os.mkdir(home+'/'+folder)
os.chdir(home+'/'+folder)
print('current dir: '+os.getcwd())
#sets array variables
linkArr = []
urlArr = []

#sets url to get data
url = input('URL containing PDF links: ')

while url.startswith('http') == False:
    url = input('Please put the URL with the protocol.. hint. https:// or http:// : ')

urlArr = url.split('/')

#get site
protocol = urlArr[0]
site = urlArr[2]

#get data
response = requests.get(url,verify=False)

#sets htmlParser Params
from html.parser import HTMLParser
class dataParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == "href" and value.endswith('pdf'):
                    print('Found '+value+'. Adding to que')
                    linkArr.append(value)

#parses data
parser = dataParser()
parser.feed(response.text)
for item in linkArr:
    iArr = item.split('/')
    filename = iArr[-1]
    if item.startswith('http'):
        link = item
    elif item.startswith('.'):
        link = url+item
    elif item.startswith('/'):
        path = site+'//'+item
        path = path.replace('//','/')
        link = protocol+'//'+path
    else:
        link = protocol+'//'+site+'/'+item
        print('no prefix logic. Trying: '+link)

    if os.path.exists(item):
        print(item + 'exsits; skipping.')
    else:
        print('starting download of '+ item)
        itemURL = link

        def download_file(itemURL):
            r = requests.get(itemURL, stream=True)
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return filename
        download_file(itemURL)
        print(filename+' saved')

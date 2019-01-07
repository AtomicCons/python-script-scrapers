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
#check if direcotry exists
if os.path.exists(home+'/MagPi') == False:
    os.mkdir(home+'/MagPi')
os.chdir(home+'/MagPi')

#sets array variables
fileArr = []

#sets url to get data
url = 'https://www.raspberrypi.org/magpi-issues'

#get data
response = requests.get(url,verify=False)

#sets htmlParser Params
from html.parser import HTMLParser
class dataParser(HTMLParser):
    def handle_data(self, data):
        pdf = data.endswith('pdf')
        if pdf == True:
            print('File Found: '+data + '. Adding file to list.')
            fileArr.append(data)
            
#parses data
parser = dataParser()
parser.feed(response.text)

#checks if file exists.Downloads file if it doesn't
for item in fileArr:
    if os.path.exists(item):
        print(item+' exists. Skipping file.')
    else:
        print('starting download of '+ item)
        itemURL = url+'/'+item
        def download_file(itemURL):
            filename = item
            r = requests.get(itemURL, stream=True)
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return filename
        download_file(itemURL)

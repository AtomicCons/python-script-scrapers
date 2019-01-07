#!/bin/python3
import os
import sys
import urllib3
import requests
import html
import array
#disables ssl warning
urllib3.disable_warnings()

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
            print(data + 'is a pdf.  Adding to Array')
            fileArr.append(data)

parser = dataParser()
parser.feed(response.text)

for item in fileArr:

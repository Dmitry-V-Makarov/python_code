import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# Retrieve a tag and print a list of tags
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

# Extract span tag, count and find sum of the numbers inside tag content
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
total = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    x = tag.contents[0]
    x = int(x)
    count = count + 1
    total = total + x

print(count)
print(total)

# Scan for links, find link in a particular position, follow the link
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
rep = input('Enter count - ')
rep = int(rep)
ptn = input('Enter position - ')
ptn = int(ptn)

# Find and follow links
for i in range(rep) :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count + 1
        if count == ptn :
            print('Retrieving:', tag.get('href', None))
            url = tag.get('href', None)

# Extract integers from an XML tag and sum them up
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
y = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(y)

lst = tree.findall('.//count')

total = 0
for count in lst:
    total = total + int(count.text)

print(total)

#http://py4e-data.dr-chuck.net/comments_42.xml
#http://py4e-data.dr-chuck.net/comments_323364.xml


#Extract integers from a JSON file and sum them up
import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter URL - ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_42.json'

data = urllib.request.urlopen(url).read()
lst = json.loads(data)
com = lst['comments']

print('Retrieved URL', url)
print('Retrieved', len(data), 'characters')

total = 0
count = 0
for item in com:
    count = count + 1
    total = total + int(item['count'])

print('Count', count)
print('Sum', total)

#http://py4e-data.dr-chuck.net/comments_323365.json


#Retrienving place_id from a JSON file
#that uses an API similar to the Google Maps API

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1 : address = 'South Federal University'

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

#print(json.dumps(js, indent=4))

plc = js['results'][0]['place_id']
print('Place id', plc)


# Version 2
#Retrienving place_id from a JSON file
#that uses an API similar to the Google Maps API

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1 : address = 'South Federal University'

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode() 
#if I switch off the .decode() with # and just use .read() it will be raw JSON
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

print(json.dumps(js, indent=4))

print('=========================================================================')

headers = dict(uh.getheaders())
print(headers)

print('=========================================================================')

plc = js['results'][0]['place_id']
print('Place id', plc)
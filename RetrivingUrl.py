# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
j=0
count = int(input('Enter Count: '))
position = int(input('Enter Position: '))


while True:
    j=j+1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    i=0
    for tag in tags:
        x=tag.get('href', None)
    #     print(x)
        if i == position:
            url=x
#             print(url)
        i=i+1
    if j == count:
        break
print(url)

import urllib.request, urllib.parse, urllib.error
import json
import ssl
from urllib.request import urlopen

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
html = urlopen(url, context=ctx).read()
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('Count:', len(info))
x=info['comments']
sum=0
for i in x:
    sum=int(i['count'])+sum
print('Sum:', sum)

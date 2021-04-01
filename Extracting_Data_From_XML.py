import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from urllib.request import urlopen

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
html = urlopen(url, context=ctx).read()
#     print(html)
parms = dict()
parms['address'] = url
if api_key is not False: parms['key'] = api_key
url1 = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url1)
uh = urllib.request.urlopen(url1, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(html)
counts = tree.findall('.//count')
#     print(counts)
sum=0
for i in counts:
#         print(i)
#         print(i.text)
    sum = int(i.text)+sum
print('Count: ',len(counts))
print('Sum: ',sum)

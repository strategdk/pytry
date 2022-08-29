# open-webpage.py

import urllib.request, urllib.error, urllib.parse

url = 'https://psykolog-andersen.dk'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

print(webContent[0:300])
import urllib 
import re

urls = ["http://google.com", "http://nytimes.com", "http://cnn.com"]
i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex) # converts regex string into something usable by regular expressions library

while i < len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)

	print titles
	i+=1

import urllib 
import re

symbolslist = ["AAPL", "SPY", "GOOG", "NFL"]

i = 0
while i <len(symbolslist):
	url = http://finance.yahoo.com/q?s=aapl&ql=1
	htmlfile = urllib.urlopen()
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_spy">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	print price 
	i+=1




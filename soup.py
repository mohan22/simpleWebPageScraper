from bs4 import BeautifulSoup
import urllib.request
import time
# r = urllib.request.urlopen('file:///C:/Users/prime/Desktop/doc.html').read()
# soup = BeautifulSoup(r,"html.parser")
# print (soup.prettify()[0:1000])
# 
prevVal=0
while 1:
	r = urllib.request.urlopen('file:///C:/Users/prime/Desktop/doc.html').read()
	soup = BeautifulSoup(r,"html.parser")
	print("Ting")
	count = 0
	for tag in soup.findAll():
	    print (tag.name)
	    if tag.name=="tr":
	    	count=count+1

	print(count);

	if prevVal!=count:
		prevVal=count
		print("Alarm")
		#Alarm
	time.sleep(10)

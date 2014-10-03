import urllib.request
import xml.etree.ElementTree as etree

page = urllib.request.urlopen("http://www.thomas-bayer.com/sqlrest/CUSTOMER/3/")
content=page.read()
content_string = content.decode("utf-8")
root = etree.fromstring(content_string)
for child in root:
	print(child.tag)
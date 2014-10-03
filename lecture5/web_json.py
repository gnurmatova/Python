import urllib.request
import json
from pprint import pprint

page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=west%20haven,%20ct")
content=page.read()
content_string = content.decode("utf-8")

json_data = json.loads(content_string)

print(json_data)
pprint(json_data)

print(json_data["coord"])
print(json_data["coord"]["lat"])

print(json_data["weather"][0]["main"])

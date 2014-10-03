import io
import re

f = open("log1.log")

regexp = re.compile(r"(?P<user>\w+)\sfrom\s(?P<ip>(\d{3}\.){3}\d{3})\sport\s(?P<port>\d{4})")

while True:
	s = f.readline()
	if not s:
		break

	for (letters) in re.findall(regexp, s):
		print(letters)
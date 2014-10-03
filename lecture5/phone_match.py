import re

regexp = re.compile(r"^\(?(?P<area>\d{3})?\)?-?(?P<number>\d{3}-\d{4}$)")

result = regexp.search("(203)444-3453")

print(result.group("area"))
print(result.group("number"))

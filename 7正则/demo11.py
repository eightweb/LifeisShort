import re

s = 'A8Cd8w58rg5s'

def convert(value):
  matched = value.group()
  if int(matched) >= 6:
    return '9'
r = re.sub('\d', convert(s), s)
print(r)
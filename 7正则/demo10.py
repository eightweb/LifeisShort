'''
  正则替换  re.sub()
'''

import re

def cof(value):  # 传入的就是 被匹配到的
  m = value.group()
  return '!!' + m + '!!'

lan = 'pyhtonC#javaPhp'
# r = re.sub('C#','go', lan, 0) # 把 C#改成 go   0是全替换 可以写成1,2,3,4... 替换1,2,3,4...次
# print(r) # pyhtongojavaPhp

r1 = re.sub('C#', cof , lan, 0)
print(r1)

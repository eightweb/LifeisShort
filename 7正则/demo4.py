'''
  概括字符集
    \d \D 就是
    \w 即匹配 数字 又匹配 字母
'''

a = 'Python111java67@#$.___,12!$88php'
import re

r = re.findall('\d',a)  # 找到 数字 0-9  等同于  re.findall('[0-9]',a)
r1 = re.findall('\D',a)  # 找到 非数字   等同于  re.findall('[^0-9]',a)
r2 = re.findall('\w',a)  # 找到 数字 + 字母      re.findall('[A-Za-z0-9]',a)
print(r2)
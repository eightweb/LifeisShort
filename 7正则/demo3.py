'''
  字符集
  r = re.findall('a[cf]c',a) 出现在 [] 里面的 是 或 的关系
  ^ 取反的意思
'''

a = 'abc,acc,adc,aec,afc,ahc'
import re

r = re.findall('a[cf]c',a)  # 找到 单词中的 中间 是b 或者是f的字符
r1 = re.findall('a[^cf]c',a)  # 找到 单词中的 中间 不是b 或者不是f的字符
r2 = re.findall('a[c-f]c',a)  # 找到 单词中的 中间 是c-f的字符
print(r)   # [acc, afc]
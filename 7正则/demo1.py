'''
  一个特殊的字符序列, 实现快速检索文本, 替换文本
  Python有一个模块 re 是用于正则的
'''

# 例题: 检测 字符串中 是否 包含某个字符
a = 'c|c#|java|c++|Python|javascript'

# a.index('Python') > -1 # 如果 > -1  包含 python , 否则不包含

# 'Python' in a  # 同样返回是否包含 


import re  # python内置的正则模块

# 用法:
# re.findall('正则表达式', '字符串')

r = re.findall('Python', a) # 搜索字符串a 是否包含python
print(r) # ['Python'] 返回一个列表

if len(r) > 0:
  print('至少包含一个Python')
else:
  print('并不包含')
'''
  边界匹配
'''
import re

qq = '1000000001'  # 10位数
r = re.findall('\d{4,8}', qq)     # 相当于是寻找 寻找 从左到有挨个匹配 满足条件之后 得到  10000000
r1 = re.findall('^\d{4,8}$',qq)   # ^开头 &结尾  就是全匹配  完全去匹配 查看 100000001是否满足条件 而不是从左到右 看是不是有满足的
print(r1)
print(r)
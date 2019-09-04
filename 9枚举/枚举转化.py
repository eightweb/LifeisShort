'''
  枚举转化, 通过具体的数据, 得到真正的枚举类型
'''

from enum import Enum

a = 1

class Vip(Enum):
  YELLOW = 1
  BALCK = 2
  GREEN = 3

print(Vip(a))  # Vip.YELLOW  通过数值, 得到真正的枚举类型
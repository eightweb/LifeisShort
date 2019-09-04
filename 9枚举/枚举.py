'''
  枚举是个类
  需要先导入 enum包
  枚举可循环
'''

from enum import Enum

class Vip(Enum):  # 所有类都是 Enum类的子类
  Red = 1
  Yellow = 2
  Green = 3
  Black = 4

print(Vip.Red) # Vip.Red 并不是打印 1 

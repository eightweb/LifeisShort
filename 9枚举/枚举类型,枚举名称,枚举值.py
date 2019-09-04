from enum import Enum

class Vip(Enum):  # 所有类都是 Enum类的子类
  Red = 1
  Yellow = 2
  Green = 3
  Black = 4


print(Vip.Red.value)        # 枚举值
print(Vip.Red.name)   # 枚举名  Red
print(Vip.Red)        # 得到 类型 Vip

for item in Vip:
  print(item)
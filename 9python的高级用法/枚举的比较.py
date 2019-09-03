from enum import Enum

class Vip(Enum):  # 所有类都是 Enum类的子类
  Red = 1
  Yellow = 2
  Green = 3
  Black = 4

class Vip1(Enum):  # 所有类都是 Enum类的子类
  Red = 1
  Yellow = 2
  Green = 3
  Black = 4


result = Vip.Black == Vip.Black
result1 = Vip.Black == 1
result2 = Vip.Black > 1
result3 = Vip.Black is Vip.Black

print(result)   # True
print(result1)  # False
print(result2)  # error  枚举类型不支持大小比较
print(result3)  # True  枚举类型不支持大小比较


print(Vip == Vip1) # False
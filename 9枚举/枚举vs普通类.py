'''

'''

from enum import Enum  # 导入枚举包中的类

# 下述的来表示类型的缺点 : 1. 可更改  2. 没有防止相同值的功能 (value值都可以相同, Enum是不可以相同的)

black = 1
red = 2

{'black': 1, 'red': 2}

class TypeCo():
  black = 1
  red = 2


class Vip(Enum): # Vip类继承了Enum类
  black = 1
  red =2

Vip.black = 3  # 报错 不允许修改




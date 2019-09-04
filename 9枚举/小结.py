'''
  强制要求,枚举下的类 是int类型, 不允许其他类型

  IntEnum  ===>>>  只能是int类型
  Enum     ===>>>  随意类型
  unique   ===>>>  不允许有相同的值
'''

from enum import Enum    # 随意类型
from enum import IntEnum, unique # 只能是int类型


class Vip(Enum):  # 所有类都是 Enum类的子类
  Red = 1
  Yellow = 'str'
  Green = 3
  Black = 4

@unique  # 加上这个装饰器 就不允许 有相同的值
class IntVip(IntEnum):
  RED = 1
  GREEN  = 1 # 报错 有相同值
  BLACK = 'SRr'   # 报错 只允许int类型
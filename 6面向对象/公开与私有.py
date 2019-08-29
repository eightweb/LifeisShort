
'''
没有绝对的私有:

  私有变量 __变量名 即可 外部不能访问
  但是外部不是绝对不能访问, 因为私有变量的底层 是py改了变量名
'''


class Pub_Pra():
  __privateNum = 10 # 私有的变量 外部不能访问

  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __priDef(self, name, age):
    print('这是私有的方法')

pub = Pub_Pra('tw', 24)

# print(Pub_Pra.__privateNum) # 报错
print(pub.__dict__) # 会发现 python把私有变量的名字 改成了 _类名__私有变量名 所以外部直接访问私有变量名 是报错的
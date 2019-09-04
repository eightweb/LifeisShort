'''
  如果不使用 global关键字 在第十行 py会认为 origin被赋值, 说明在go函数中定义了 不会往全局找,
  然而发现 go()函数中 并没有变量 origin 就报错


  global 与 nonlocal 的区别

  1. global 在任何地方, 任何地点声明, 把变量声明为, 全局
  2. nonlocal 用于在 嵌套函数中, 当内部函数使用外层函数的变量时, nonlocal 变量, 就可获取到最外层函数的变量

  def outside():
    msg = 'aaaa'
    def inside():
      msg = 'bbb'
    print(msg)   # 打印 aaa 因为 函数 inside内部有msg变量,修改的也是内部的, 即使我们认为去找外层的变量

  def outside():
    msg = 'aaaa'
    def inside():
      nonlocal msg   # 告诉python 不用再定义变量了, 就使用外部的函数 outside()函数的msg吧
      msg = 'bbb'    #  打印 bbb 
    print(msg)  
'''
origin = 0

# 非闭包实现 实现实时累加
# def go(step):
#   global origin 
#   new_pos = origin + step
#   origin = new_pos
#   return new_pos

# print(go(2))
# print(go(6))



# 闭包实现
# pos 一开始的步数
# new_pos 新的步数
# step 走的步数

def factory(pos):
  def go(step):
    nonlocal pos   # 告诉 python 不用再去定义pos了 去找外部函数 factory中的 pos吧
    new_pos = pos + step
    pos = new_pos
    return pos
  return go 

tou = factory(origin)
print(tou(2))
print(tou(3))
print(tou(5))

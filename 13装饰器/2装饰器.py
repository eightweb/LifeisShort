
'''
  需求: 每次调用函数的时候, 打印当前调用的时间
'''

import time

def f1():
  print('This is function1')


def f2():
  print('This is function2')


# def print_current_time(fun):
#   print(time.time())
#   fun()
# print_current_time(f1)  


# 装饰器 deco看似被调用, 但实际解决问题的是wrapper函数 deco装饰了wrapper
# 形成了闭包
def deco(func):
  def wrapper():
    print(time.time())
    func()
  return wrapper

f = deco(f1)
f()

# ==========================上述的 跟 1装饰器.py 差不多 调用太多 都没解决实际情况

'''
  python 对装饰器加上语法糖 @符号
'''

import time


def deco(func):
  def wrapper():  
    print(time.time())
    func()
  return wrapper


@deco
def f1():
  print('This is function1')


def f2():
  print('This is function2')


# ==========函数加上了 @语法糖 直接调用 就可以实现 2装饰器的功能 不需要调用多次 只需要调用原来的函数就可有

f1()
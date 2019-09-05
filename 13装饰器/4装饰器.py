
'''
  当函数带有参数的时候, 改造装饰器

  不同的函数,参数的个数不同,  使用python的 可变参数

'''


import time

def deco(func):
  def wrapper(*args):  # 可变参数, 适用于 有不同 参数个数的函数
    print(time.time())
    func(*args)
  return wrapper


@deco
def f1(name):
  print('This is function1' + name)

@deco
def f2(name, age):
  print('This is function2', name, age)


def f3(name, age, ss):
  print('This is function2', name, age, ss)


f1('xiaoming')
f2('小明', 12)
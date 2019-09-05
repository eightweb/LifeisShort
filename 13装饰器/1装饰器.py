

import time

# 问题 : 现在需要在函数调用时, 加上调用时的 当前时间 , 1个 两个函数是没事 , 假如有100个 1000个函数呢
# 对修改是封闭的, 对扩展是开放的

def f1():
  print('This is function')


def f2():
  # print(time.time())
  print('This is function')


# =====================为了解决上述的问题 ======================================

# 专门写一个函数 来实现需求 接收一个函数当做参数,并执行
def print_current_time(fun):
  print(time.time())
  fun()

print_current_time(f1)
print_current_time(f2)



# ===================================但是不够简洁, 见2装饰器.py===================================
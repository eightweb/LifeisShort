'''
  序列解包与链式赋值
'''
a = 1
b = 2
c = 3

#写成
a,b,c = 1,2,3

d = 1,2,3  # 序列解包  此时d的类型是tuple 等于(1,2,3)
# 再
a,b,c = d

# import global关键字
from global关键字 import c

print(c)
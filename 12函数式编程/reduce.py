'''
  reduce 在python3中已经不是全局的命名空间了, 想要用 先引用

  reduce(funciton, 序列, 初始值=None) 如果初始值是10 第一次调用的时候 x 取值 就是10

  作用: 连续计算(不是连续相加), 连续调用 第一个参数 function

  运算过程:
          1. 第一次调用, 取list_x中的 1 当做 x值,  2 当做 y值 计算 得到 3
          2. 第二次调用, 取上一次得到的值 当做 x值,  取list_x中的 3 当做 y值 得到 6
          3. 以此类推...一直得到最后

          (((((1 + 2) + 3) + 4) + 5) + ...)
'''

from functools import reduce

list_x = [1, 2, 3, 4, 5, 6, 7, 8]

r = reduce(lambda x,y: x + y, list_x)

print(r)

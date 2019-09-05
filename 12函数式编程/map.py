'''
  map是一个class类, 对于传入的集合里的每个元素, 都传入到function中

  map(function, 集合 (可传入多个集合))

  适用场景: 循环处理数据时,可以用的到
'''

# 求list_x列表每个元素的平方 得到一个新的列表

list_x = [1, 2, 3, 4, 5, 6, 7, 8]

def f1(x):
    return x * x

list_y = map(f1, list_x)

print(list(list_y)) # [1, 4, 9, 16, 25, 36, 49, 64]
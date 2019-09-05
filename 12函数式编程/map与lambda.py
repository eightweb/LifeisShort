'''

'''

# 求list_x列表每个元素的平方 得到一个新的列表

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_a = [1, 4, 9, 16, 25, 36, 49, 64]

list_y = map(lambda x: x * x, list_x)  # 第一个参数, 传入lambda匿名函数

print(list(list_y))  # [1, 4, 9, 16, 25, 36, 49, 64]


list_z = map(lambda x, y: x * x + y, list_x, list_a)

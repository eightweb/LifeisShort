'''
  过滤
    filter(function, 序列)

    filter的函数返回的是 真 or 假 不是具体值 所以下面的实例 返回的是 6,7,8
'''
list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def filter_fn(x):
    return True if x > 5 else False


x = filter(filter_fn, list_x)

print(list(x))

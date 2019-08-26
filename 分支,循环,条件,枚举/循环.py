# 常见的两个循环  while  for

# while会重复执行代码块 容易造成死循环
condition = 1
while condition <= 10:
  print(condition)
else:
  print('只有当不满足条件时, 就执行 else语句')


# for循环 用来遍历 / 循环 序列 集合 和 字典
 
a = [1,2,3,4]
for item in a:
  if item == 2:
    break # 终止循环
    # continue # 跳出当前循环
  print(item, end=',')
else:
  print('只有当循环结束之后, 才能执行else语句, 基本上就只写for ')


# 重复指定次数的循环
# range(index, length, 间隔多少) 函数 生成指定长度的序列
for item in range(0, 10, 2): # 自 0 开始 循环十次
  print(item)
a = 'c2345c#5322java@4234c++422Python867javascript'


import re

# 只要查询是否包含 0-9的数字就行了   \d 就表示 0-9   \d这种叫做元字符  python这种 叫普通字符

r = re.findall('\d', a)  # 把 a 字符串所有的数字 提取出来

r1 = re.findall('\D', a) # 把 a 字符串所有的非数字 提取出来

print(r)
print(r1)

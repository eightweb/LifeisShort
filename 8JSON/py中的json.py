'''
  JSON : JSON是一种轻量级的数据交换格式
        字符串就是JSON的表现形式

  JSON字符串: 符合JSON格式的字符串    {"name": "xiaoming"}  

  跨语言的, 在任何语言中, 都有

  loads()方法 是把json转化成对象的内置方法      序列化
  dumps()方法 把其他数据格式转化为JSON          反序列化
'''

import json  # python中内置的模块 操作json的

json_str = '{"name": "tw", "age": 19}'
list_str = [
  {'name': '12', 'flag': False},
  {'name': '12', 'flag': True},
]
student = json.loads(json_str)
json_str = json.dumps(list_str)

print(type(student))  # dict类型
print(student['name'])

print(type(json_str))
print(json_str)
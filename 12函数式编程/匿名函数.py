'''
  lamdba 关键字
                   参数        逻辑( :冒号后面 只能是  简单的表达式)
  表现形式 : lambda parameter: expression

  调用: 赋值给一个变量, 调用变量
  
  注意 : 不需要 return结果 他的表达式 就是return
'''

def add(x, y):
  return x + y

add(1,2)
f = lambda x,y: x + y

f(1,2)
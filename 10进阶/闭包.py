'''
  闭包: 函数 + 环境变量(函数定义的时候) 不受外部的变量所影响
  意义: 保存了当时定义的环境, 包括变量
  作用: 不影响全局变量, 避免全局污染
  
  下面的例子: 
    cur()函数定义了一个变量 a = 25
    cur()函数下有个cur_son() 使用到了 a变量
    此时, cur_son()的环境变量,就是 函数 cur()的内部
    返回cur_son()函数
  
  调用cur_son() 此时cur_son()的环境变量是 cur() 所以a变量 也是cur()内部的a变量
  不受 全局变量 a的影响
'''


def cur():
  a = 25
  def cur_son(x):
   return  a * x * x
  
  return cur_son

a = 10
f = cur() # 此时的f就是 cur_son函数
print(f.__closure__)
print(f(2)) 




'''
  打印的还是18 不是28 不受全局变量影响, 形成闭包

  introduce() 的环境变量是fa()函数 (包括了 age)
'''
def fa():
  age  = 18
  
  def introduce(name):
    return f'my name {name}, today,{age}' 
  
  return introduce


age = 28
my = fa()

print(my('xm'))

'''
def FunctionName(args):
    pass

  def是关键字 函数名(参数):
    占位符
  
  1. 参数可以没有, 参数可以有默认值
  2. 要有return 返回, 如果没有 就返回None
'''

def Summation(num1, num2 = 10):
    return num1 + num2

def damage(sk1, sk2):
  return sk1 * 2, sk2 * 4   #  返回元组
    
print(Summation(10, 20))

skill_damage, skill_damage1 = damage(2, 4);  # 用两个变量 接收函数返回的数据   (js的解构赋值) (py中叫序列解包)
print(skill_damage, skill_damage1)
'''
  函数参数:
      必须参数
      关键字参数: 不比关心函数的形参的顺序, 调用时, 指定实参对应的是形参的哪个
'''
def Summation(num1, num2):
    return num1 + num2
  
c = Summation(num2 = 10, num1 = 30)  # 使用的是关键字参数, 不比考虑形参的顺序位置



'''
  默认参数
'''
def defaultDef(num1, num2 = 10):
    return num1 + num2
  
c = defaultDef(2)  # 当不传的时候 num2 默认是10



'''
  可变参数: 随便传 不用管形参的多少 (也可以不传)
    比如print(1,2,4,5,6,6) 可以传递无数的参数

  实际实现方式: 形参处理成tuple类型 永远是看成一个参数
              所以我们可以自己调用的时候 传个tuple就行了 

              demo((1,2,3,4,5,6))  
'''
def demo(*params):
  print(params)
  print(type(params))

demo(10,2,4,5,'22')


'''
  如果: 我就想传入个元组到函数里面
  实参加上*
'''
def demo1(*params):
  print(params)

demo1(*(1,2,3,4))



'''
  必须参数, 可变参数, 默认参数 共同组成的函数

  一般不要设计这种函数, 太麻烦了
'''
def Form(params, *params1, params2 = 2):
  print(params)
  print(params1)
  print(params2)

Form(2, 1,2,4, params2='22')  # 指定 params2为新的参数, 要不然永远都是在可变参数中 应为是元组类型


'''
  打印字典的key value值 items()函数
  values()函数 专门打印value值
  keys()函数 专门打印key值
'''
def city_temp(**param):
  for item,value in param.items():
    print(item, ":", value)

city_temp(bj='32c', sh='21c', hf='23c')
'''
  类名需要大写, 使用驼峰命名规则
  类可以定义变量(数据成员) 函数

  调用类 需要实例化

  注意:
      1. 在类下编写函数,与普通模块下编写函数是不同的, 在类中, 函数的参数需要加上固定的关键字self
      2. 在类中定义的变量, 相对于类内部来说 不是全局变量, 想要访问变量, 需要加上self.变量名访问

  类的浅显的理解: 对函数与变量的封装
  类只负责定义, 不负责执行


  类的传参:
      1. 在py中, 在类中直接写形参是不行的, 需要特殊的函数(构造函数) __init__ 来接收
      2. __init__是自动调用, 不需要我们自己去调用
      3. 我们也可以自己去显示调用, 返回 None 类型是 NoneType, 不能返回除None外的其他类型

  类变量与实例变量:
    实例变量:
        1. 与对象相关, 对象由模版创建, 由 __init__函数中的 self.变量名来定义实例变量
    类变量:
        1. 在类中的变量
'''

class Student():
  name = ''
  age = 0

  def __init__(self, name, age): # 这边写多少参数, 外部就需要传多少实参
    # 根据外部的实参,来初始化对象的属性 (根据外部的参数, 来给内部的变量赋值)
    self.name = name  
    self.age = age
    pass

  def do_homework(self):
    print(self.name,":", self.age)



student = Student('我是name', 12) # 类的实例化, 在py中 不需要 new关键字
print(student.name, 'ssss')   # 访问类的内部变量
student.do_homework() # 调用类的方法


stu1 = Student('石敢当',18)
print(stu1.name)
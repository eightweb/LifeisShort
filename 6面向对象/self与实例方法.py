'''
  self特性: self可以叫任何名称,如 this
    1. 在类中, 倘若写一个实例方法的话, 在方法的参数中, 固定写一个self关键字
    2. 在调用实例方法的时候, 是不需要对self传参的
  
  实例方法:
    实例可以调用的方法, 如最后一行的homework 通过 stu.homework()调用了 就是实例方法
  
'''


class Student():
  sum = 0
  name = ''
  age = 12

  # 实例方法
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print(name)
    print(age)

  def homework(self):
    self.sum+=1
    print(self.sum)
stu = Student('小明', 18)
stu.homework()
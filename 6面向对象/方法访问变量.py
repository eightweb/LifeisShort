'''
  在实例方法中,访问实例变量与类变量

  1. 访问类变量   类名.类变量   Student.sum
  2. 访问类变量    self.__class__.类变量   self.__class__.sum
'''

class Student():
  sum = 0   # 类变量
  name = ''
  age = 12
  hh = '22'
  def __init__(self, name, age):
    self.name = name   # self.name 就是实例方法中访问实例变量了
    self.age = age
    print(name)     # 这个name 是读取的形参 不是 读取类变量  所以name 与 self.name 不是一个东西
    print(Student.sum) # 在实例方法中访问类变量
  def homework(self):
    self.sum+=1
    print(self.sum)   # self.sum 访问的实例变量
    print(Student.sum)  # 类名.类变量 访问的才是 类变量


stu = Student('小明', 18)
stu.homework()
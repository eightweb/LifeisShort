'''
  静态方法与类方法 访问 实例变量 会报错
'''

class Studen():
  sum = 10

  # 实例方法
  def __init__(self,name,age):
    self.name = name  
    self.age = age
    print(self.name) # 实例变量
    # Studen.sum+=1    # 实例方法操作类变量
    print(self.age)


  # 类方法
  @classmethod
  def plus_sum(cls):
    cls.sum+=1
    print(cls.sum)

  # 静态方法
  @staticmethod
  def add(x,y):
    print(Studen.sum)   # 静态方法 访问 类变量
    print('this is staticMethods')

stu = Studen('小米', 28)
stu.add(1,3)      # 实例对象调用
Studen.add(0,3)   # 类调用
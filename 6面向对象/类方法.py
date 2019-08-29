'''
  类方法: 直接方法类变量的方法
  作用: 操作类变量的
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


# 类方法的调用
stu = Studen('石敢当', 18)
Studen.plus_sum() # 类名调用
stu.plus_sum()  # 实例名调用 不建议 但是允许
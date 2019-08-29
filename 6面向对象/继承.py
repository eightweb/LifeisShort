'''
  继承性
    特点: py允许多继承
    作用: 1. 避免定义重复的方法与变量
    用法: 在 子类的 参数列表中 添加 父类的类名
    注意: 1. 子类传给父类的变量中, 通过__init__ 需要把self带上    (不推荐)
          2. super关键字  (super代表的就是父类)

    过程:
        1.子类继承父类
        2.通过子类的实例对象 统一接收 子类与父类所需要的参数
        3.经过子类的__init__的时候, 通过super关键字 接收父类所需要的参数, 传给父类
        4.此时, 父类已经有参数了, 方法都可以调用了

        vs   JavaScript
        1,2,4 都相同与py 只不过第3步的 __init__ 换成了 constructor
  封装性
  多态性
'''
class People():
  sum = 0
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_name(self):
    print(self.name)


class Studen(People):
  # sum = 0
  def __init__(self, school, name, age): # school 是子类的  name age 是父类的 实例变量
    super(Studen, self).__init__(name, age)  # 子类调用父类的实例方法 并把参数传入 优先使用
    # People.__init__(self, name, age)  # 通过显示调用父类的构造函数 把参数传给父类 (必须传self给父类)
    self.school = school  # 子类定义一个 实例变量 父类也要传 实例变量
    pass

  def homeWork(self):
    print('homework')


stu = Studen('山中', '高三', 12)
stu.get_name()
  



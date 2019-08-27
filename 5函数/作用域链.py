'''
  作用域具有链式的

'''

c = 1
def fun1():
  c = 2
  def fun2():
    c = 3
    print(c)
  fun2()

fun1()

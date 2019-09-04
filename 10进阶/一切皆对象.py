
'''
  一切皆对象: 在py中,一个变量可以赋值任意类型 (int  str boolen def class 等)
'''

# A函数 作为 B函数的参数

def A():
  return 'A'

def B(reg):
  print(reg)

B(A())
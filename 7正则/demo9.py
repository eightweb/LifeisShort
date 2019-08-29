'''
  组
'''
import re

a = 'pythonpythonpythonpythonpython'

r = re.findall('(python){3}(JS)',a)
print(r)
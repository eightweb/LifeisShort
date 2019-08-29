'''
  数量词
'''

a = 'python111java67@#$.___,12!$88php'
import re
                    # 匹配到 最少 3 个 最多 6个的字符
r = re.findall('[a-z]{3,6}',a)  # 匹配到三个字母为一组的字符串
print(r)

'''
  数量词的其他表现形式

  * 匹配 * 前面的字符 0次 或者 无限多次
  + 匹配 1次 或者 无限多次
  ? 匹配 0次 或者 1次
'''

a = 'pytho0python111pythonn'
import re
                 
r = re.findall('python*',a)  # *前面是n pytho满足0次 python满足1次 pythonn满足两次 都满足于 0-无限多
r1 = re.findall('python+',a) # +前面是n  至少要出现一次n
r2 = re.findall('python?',a) # ?前面是n  0次 或者 1次
print(r) # ['pytho', 'python', 'pythonn']
print(r1) # ['python', 'pythonn']
print(r2) # ['pytho', 'python', 'python']  # pythonn 被匹配python的时候 满足条件 后面的就去掉了

'''
  与读文件一样
    1. 打开文件, 如果没有, 创建文件
    2. 指定编码格式

  with open('路径', 'w', encoding='编码格式') as 重命名:
    重命名.write('写入的内容')

注意: 如果是 w 每次调用 都是重新覆盖之前的文件, 如果我们想要的是文件内容追加
      把 w 改成 a  (append)追加模式
'''


# 写文件 (没有就创建)
# with open('./被写的文件.txt', 'w', encoding='UTF-8') as w_file:
#   w_file.write('我是被写入的1')


# 追加文件内容
with open('./被写的文件.txt', 'a', encoding='UTF-8') as a_file:
  a_file.write('\n我是被追加的字')


# 读文件
with open('./被写的文件.txt', 'r', encoding='UTF-8') as r_file:
  print(r_file.read())
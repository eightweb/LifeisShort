
''' 
  r 代表读取的是文本文件                                           错误时   忽略
      python中内置函数 open('路径', 'r', encoding='文件编码', errors='ignore') 打开文件
      文件打开后 通过   read()函数       读取内容
      文件操作完毕,     close()函数      关闭文件

      read(size) size: 字节大小
      readline()       读取文件中的一行
      readlines()      一次读取所有内容并按行返回list

      
  rb 代表读取的是 图片, 视频的 二进制文件
    python中内置函数 open('路径', 'rb') 打开文件
  

=================<<<<<<<<<<<<<<但是>>>>>>>>>>>==================
  每次读取文件都close 太麻烦 python内置 with open('路径', 'r') as fileName自动关闭文件

  try: 
    逻辑代码
  except:
    try中出错, 直接走这里
  finally:
    不管出错不出错, 都走
'''

# try:
#     f = open('./file.text', 'r')
#     print(f.read(1))
#     print('======================================')
# except:
#   f.close()       # 文件操作完毕, 必须关闭, 会占资源
# finally:
#   f.close()       # 文件操作完毕, 必须关闭, 会占资源
  # print(f.read())  # 文件关闭后, 不可进行操作


# with open('./file.text', 'r', encoding='UTF-8') as fileName:
  # print(fileName.read(200))
  # print(fileName.readline()) # str类型
  # print(fileName.readlines())
  # print(type(fileName.readlines())) # list类型


with open('./bgc.jpg', 'rb') as jpg_file:
  print(jpg_file.read())      # 读取的是图片 返回的是 16进制表示的字节




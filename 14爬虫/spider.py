
from urllib import request
import re
''' 
  urllib python 中内置的模块, 用于发送请求
  request.urlopen(url) 接收发送请求的地址


  ([\s\S]*?)  这是正则 自己查
  []
  \s \S
  ()          是组的概念 自己查
  *
  ?           贪婪 非贪婪模式


  正则分析html                         
            1. 先获取 <span class="txt">([\s\S]*?)</span>是包含整个数据 (主播名称 + 主播人气的)
'''


class Spider():
    url = 'https://www.huya.com/g/lol'
    root_pattern = '<span class="txt">([\s\S]*?)</span>'
    name_pattern = '<i class="nick" ([\s\S]*?)</i>'  # 匹配名字

    # 私有方法, 获取内容的方法
    def __fetch_content(self):
        r = request.urlopen(Spider.url)  # 读取类变量
        htmls = r.read()   # 返回字节码数据 bytes 需要转化为字符串
        htmls = str(htmls, encoding='utf-8')  # 转化字节码为字符串
        # 读取的数据, 写入到文件中
        # with open('./htmls.html', 'w', encoding='UTF-8') as w_htmls:
        #   w_htmls.write(htmls)

        return htmls  # 这边rerun出去 可以让go标签能赋值 要不然报错

    # 入口方法, 可供外部调用

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)   # 传给分析函数

    # 分析标签方法

    def __analysis(self, htmls):
        root_html = re.findall(self.root_pattern, htmls)  # 正则获取字符串 获取的是多个
        anchors = []
        for item in root_html:
            name1 = re.findall(self.name_pattern, item)
            with open('./所有主播.txt', 'a', encoding='UTF-8') as name:
                name.write(str(name1) + '\n')
            anchors.append(name1)
        # print(anchors) # 所有主播的名字


spider = Spider()

spider.go()  # 调用入口方法

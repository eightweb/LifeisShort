# 第一种导入方式 导入其他的模块(文件)
import t.c1 as m 
# import 模块(文件)的路径 as 重命名

# 变量的访问 需要通过文件名.出来
print(m.a)



# 第二种导入方式, 导入模块内的具体的变量 函数等
# from module_name import a,def
from t.c1 import a
print(a)

# 第三种导入方式,  直接导入模块
from t import c1
print(c1.a)


# 第四 通过 * 一次导入模块内所有变量, 配个__all__使用
from t.c1 from *
print(a)
print(b)

# 第五  通过 逗号分隔 引用模块中的多个变量
from c3 import name, age
# 当引用的变量特别多 
# from cxx import (a, b, c,
# d)
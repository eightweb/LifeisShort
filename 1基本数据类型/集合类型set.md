# 集合({}) set类型,  序列是有序的
## 定义一个 空的几个  set() 就行了

特点: 
  1. 无序, 就等于 无 index  无切片操作
  2. 无重复值  {1,1,2,2}  返回 {1,2}
type({1,2,3,4}) ===>> set 类型

obj = {1,2,3,4,5};

2. 操作:
  len({1,2,3})   ===>> 3
  3 in {1,2,3}        true
  3 not in {1,2,3}    false

  两个集合的差集
    {1,2,3,4} - {1,2}   ====>>> {3, 4} 

  两个集合的交集
    {1,2,3,4} & {2,3}  =====>>> {2,3}

  集合的相加及其去重  (并集)
    {1,2,3,4} | {2,3,4,5} ====>>> {1,2,3,4,5}
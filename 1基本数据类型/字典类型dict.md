# 字典类型  dict, 就是对象类型 是 key value 组成
##  字典类型也是个集合, set类型只有value  dict有key value组成
## 字典中 不能有重复相同的key, 后面的会覆盖前面的

## key必须是不可变 (int str tuple )的类型, value是任意类型

## 空的字典 {} 表示
{
  key: value,
  key1: value1
}

dic = {
  'Q': '这是Q',
  'W': '这是W',
  23: '这是23'
}
操作: 
  访问 通过key访问value值

  dic['Q'] ===>> '这是Q'
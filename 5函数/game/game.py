'''
  要求: 计算 合成的六级石头 与 购买的六级石头  谁更划算
'''

'''
  购买1级石头
'''
l1_value = 0.75 # 1个1级石头 0.75金
l1_value_diamond = 8 # 1个1级石头同时消耗8个钻石


'''
  1级合成3级
'''
l1_to_l3  = 12 # 3级 = 1级(12个)
l1_to_l3_gold = 0.39 # 同时消耗 0.39金
l1_to_l3_vit = 10 # 同时消耗 10点体力


'''
  3级合成4级
'''
l3_to_l4 = 16  # 4级 = 3级(1个) + 1级(16个)
l3_to_l4_gold = 0.897  # 还需要消耗 0.897金
l3_to_l4_vit = 10 # 消耗体力10
l3_to_l4_rate = 0.4878 # 成功概率 0.4878
                # 失败 金和1级 扣除 不消耗体力


'''
  4级合成6级
'''
l4_to_l6 = 12 # 6级 = 4级(12个)
l4_to_l6_gold = 19.75 # 消耗19.75金
l4_to_l6_vit = 10 # 体力消耗10




'''
  6级 = 750金
  1钻石 = 0.05金
  1体力 = 1金

是自己合成划算, 还是购买划算
'''
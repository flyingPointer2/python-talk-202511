# 元组简介

point_tuple = (3, 4, 5)

# 可以通过索引访问元组中的元素，其规则与列表一致
print(point_tuple[0])
print(point_tuple[0:2])

point_list = [3, 4, 5]
point_list[2] = 99
print(point_list)

# 错误代码示例：
# point_tuple[2] = 99 # TypeError: 'tuple' object does not support item assignment 

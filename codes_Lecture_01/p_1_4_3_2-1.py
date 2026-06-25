# 集合简介(1)

data = [1,1,2,3,5,13,34,3]

my_set = set(data)
print(my_set)

print('集合的元素个数为：', len(my_set))

my_set.add(666)
print('增加元素666后，集合为：',my_set)

my_set.discard(13)
print('删除元素13后，集合为：',my_set)


# 列表的常用方法举例(1)

names = ['喜羊羊', '美羊羊', '懒羊羊', '沸羊羊']

print("列表中的元素个数 = ", len(names))

# 增加元素

names.append('慢羊羊')
print(names)

names.extend(['红太狼', '灰太狼'])
print(names)

names.insert(2, '刀羊前辈')
print(names)

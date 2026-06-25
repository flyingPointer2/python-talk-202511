# 参数传递机制
# (2) 可变对象举例

x = [1,1,2,3,5]
print(f'id(x) = {id(x)}')

x.append(8) # 列表末尾新增一个元素
print(f'id(x) = {id(x)}')

def make_things_zero(v):
    """ 将列表的所有元素改为0 """
    for i in range(len(v)):
        v[i] = 0

x = [1,1,2,3,5,8,13]
make_things_zero(x)
print(x)

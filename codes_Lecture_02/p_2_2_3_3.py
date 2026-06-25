# 参数传递机制
# (3) 列表作为函数参数举例

def make_things_zero(v):
    """ 将列表的所有元素改为 0 """
    for i in range(len(v)):
        v[i] = 0

x1 = [1,1,2,3,5,8,13]
x2 = [21,34,55,89,144]

make_things_zero(x1)
make_things_zero(x2[:])

print('x1 = ', x1)
print('x2 = ', x2)


# 但如果切片中包含可变对象，
#   修改这些可变对象的内容可能会影响原列表
def make_things_zero_v2(v):
    """ 将列表的所有元素改为 0 (version 2)

    假设：
    - 参数v是列表
    - 且其元素仅有整数、浮点数或者仅包含整数或浮点数的列表
    """
    for element in v:
        if type(element) == list:
            for i in range(len(element)):
                element[i] = 0
        else:
            element = 0

x3 = [1,1,2,3,[5,8,13]]
make_things_zero_v2(x3[:])
print('x3 = ', x3)




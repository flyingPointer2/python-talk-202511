# 参数传递机制
# (1) 不可变对象举例

x = 1000
print(f'Define `x=1000`, id(x) = {id(x)}')  # 显示x对象的内存地址

x = x + 1
print(f'After `x=x+1`, id = {id(x)}')  # 显示新的x对象的内存地址


def add_one(v):
    v = v + 1

x = 100
add_one(x)
print(x)

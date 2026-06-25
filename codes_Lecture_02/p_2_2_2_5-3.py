# 参数传递示例5 顺序要求(3)

def test(*numbers, n):
    """ 测试函数2 任意数目位置参数之后 存在不带默认值的参数 """
    # 直接打印函数接收到的n与numbers
    print(f'n = {n}')
    print(f'numbers = {numbers}')


# 对于任意数量位置参数之后的参数，只能传入关键字实参

# test(1,2,3)    # TypeError: test() missing 1 required keyword-only argument: 'n'
test(1,2,n=3)
# test(n=1,2,3)  # SyntaxError: positional argument follows keyword argument
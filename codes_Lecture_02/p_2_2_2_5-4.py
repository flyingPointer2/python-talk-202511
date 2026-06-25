# 参数传递示例5 顺序要求(4)

def test(*numbers, n=2):
    """ 测试函数3 任意数目位置参数之后存在带有默认值的参数 """
    # 直接打印函数接收到的n与numbers
    print(f'n = {n}')
    print(f'numbers = {numbers}')


# 对于任意数量位置参数之后的参数，只能传入关键字实参

test(1,2,3)    # 能够运行，但因为三个参数都被归入numbers中
test(1,2,n=3)
# test3(n=1,2,3)  # SyntaxError: positional argument follows keyword argument
# 参数传递示例5 顺序要求(2)

def test(n=2, *numbers):
    """ 测试函数1 任意数目位置参数之前 存在带有默认值的参数 """
    # 直接打印函数接收到的n与numbers
    print(f'n = {n}')
    print(f'numbers = {numbers}')


# 对于任意数量位置参数之前的参数，只能传入位置实参

# 下面这行语句中的第一个参数 1 会被传递给 n
test(1,2,3)
# test(1,2,n=3)  # TypeError: test() got multiple values for argument 'n'
# test(n=1,2,3)  # SyntaxError: positional argument follows keyword argument
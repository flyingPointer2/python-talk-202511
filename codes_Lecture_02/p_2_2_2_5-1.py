# 参数传递示例5 顺序要求(1)

# NOTE 形参n所对应的实参须以位置参数的方式传递
def calculate_n_sum(n, *numbers):
    """ 计算传入参数的n次方的和 """
    the_sum = 0
    for number in numbers:
        the_sum += number**n
    return the_sum


print(calculate_n_sum(2, 1, 2, 3))


# 错误代码示例
# 错误原因: 对于任意数量位置参数之前的参数，只能传入位置实参

# print(calculate_n_sum(n=2, 1, 2, 3))
# print(calculate_n_sum(2, 1, 2, n=3))


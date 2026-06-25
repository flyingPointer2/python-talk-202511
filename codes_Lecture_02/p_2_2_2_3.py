# 参数传递示例3 任意数目位置参数示例


def get_square_sum(*numbers):
    """ 计算传入参数的平方和 """
    the_sum = 0
    for number in numbers:
        the_sum += number**2
    return the_sum


print(get_square_sum(1, 2, 3))
print(get_square_sum(1, 2, 3, 4))

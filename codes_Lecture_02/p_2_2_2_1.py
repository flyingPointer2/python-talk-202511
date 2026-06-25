# 参数传递示例1 位置参数与关键字参数示例

def divide(numerator, denominator):
    """ 两个实数相除 """
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("错误：除数不能为零！")
    else:
        return result

# 方式1 位置参数（positional argument）
print(divide(25, 100))
print(divide(100, 25))

# 方式2 关键字参数（keyword argument）
print(divide(numerator=25, denominator=100))

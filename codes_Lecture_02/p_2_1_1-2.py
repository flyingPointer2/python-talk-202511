# 异常处理示例1(2)

number = float(input("请输入一个正实数："))
try:
    print("1/{:.3f} is {:.3f}".format(number, 1/number))
except ZeroDivisionError:
    print("Error!")
    print("You should not input ZERO!")

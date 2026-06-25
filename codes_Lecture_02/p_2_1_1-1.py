# 异常处理示例1(1)

number = float(input("请输入一个正实数："))
print("1/{:.3f} = {:.3f}".format(number, 1/number))

# 若用户输入为0，则会抛出如下错误：
#   ZeroDivisionError: float division by zero
# 若用户输入为非数字（例如输入字符串"1o"(错把o看成0)），则会抛出如下错误：
#   ValueError: could not convert string to float: '1o' 

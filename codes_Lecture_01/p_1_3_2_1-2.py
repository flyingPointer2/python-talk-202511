# 字符串与整数或浮点数的转化举例

a = "3.14"
b = eval(a)
print("The type of a is ",type(a),"\nThe type of b is ", type(b))

a = "3.14 * (2024 - 8 * 22)"
c = eval(a)
print(a, " = ", c)

# 错误代码示例：

# print(int('3.14'))  # ValueError: invalid literal for int() with base 10: '3.14'
# print(int('hello')) # ValueError: invalid literal for int() with base 10: 'hello'

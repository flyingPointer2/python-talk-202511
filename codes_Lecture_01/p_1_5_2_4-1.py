# for循环生成列表（列表推导式 list comprehension）

# 示例1 1~10（闭区间）范围内的所有整数的平方
square_numbers = [i**2 for i in range(1,11)]
print(square_numbers)

# 示例2 1~10（闭区间）范围内的所有偶数的平方
square_numbers = [i**2 for i in range(1,11) if i%2 == 0]
print(square_numbers)


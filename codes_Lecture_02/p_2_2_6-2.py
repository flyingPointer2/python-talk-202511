# lambda 函数应用示例

# map()示例 计算列表的每个元素的立方

numbers = [1,1,2,3,5,8,13,21,34]
cubic_of_numbers = map(lambda x:x**3, numbers)

print(cubic_of_numbers)
print(list(cubic_of_numbers))

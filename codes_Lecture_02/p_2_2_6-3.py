# lambda 函数示例

# filter()示例 筛选列表中的所有偶数元素

numbers = [1,1,2,3,5,8,13,21,34]
even_numbers = filter(lambda x:x%2==0, numbers)

print(even_numbers)
print(list(even_numbers))


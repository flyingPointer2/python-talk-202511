# Python中的字符串可以以单引号、双引号或者三引号包裹

print('Hello world!')
print("Hello world!")
print('''Hello world!''')

# 其中，三引号包裹的字符串可以自由换行
print('''
Hello, 
world! 
''')
# 其余两种形式的字符串要换行需使用转义字符`\n`
print('Hello,\nworld! ')

# 错误代码示例
# print('Hello, 
# world! ')
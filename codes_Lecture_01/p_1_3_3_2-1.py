# 字符与字符串的编码和解码(1)

# 字符串与整数的“转换”关系
print("ord('A') = ", ord('A'))
print("ord('学') = ", ord('学'))
print("chr(65) = ", chr(65))
print("chr(23398) = ", chr(23398))

# 错误代码示例：
# print(chr(-1))  # ValueError: chr() arg not in range(0x110000)
# print(ord('hello')) # TypeError: ord() expected a character, but string of length 5 found


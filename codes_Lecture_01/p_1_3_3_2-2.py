# 字符与字符串的编码和解码(2)

# 字符串编码与解码举例
msg2 = "A学"
print(msg2.encode("UTF-8"))     # b'A\xe5\xad\xa6'
print(msg2.encode("GB2312"))    # b'A\xd1\xa7'

msg2_encoded_GB2312 = msg2.encode("GB2312")
print('编码前的数据类型是', type(msg2), '\n编码后的数据类型是', type(msg2_encoded_GB2312))

msg2_decode_GB2312 = msg2_encoded_GB2312.decode("GB2312")
print('解码后的数据类型是', type(msg2_decode_GB2312))

# 错误代码示例：
# msg2_encoded_GB2312.decode("UTF-8") # UnicodeDecodeError
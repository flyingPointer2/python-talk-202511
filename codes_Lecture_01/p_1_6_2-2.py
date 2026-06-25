# with open as 读写文件示例2

# 写文件
output_content = "3**24 = " + str(3**2024)
output_list = [
    '\nIt was the best of times,\n',
    'it was the worst of times\n'
]

# 以写入模式打开文件。文件不存在则创建，存在则覆盖。
with open("data/example_output_text.dat","w") as f:
    f.write(output_content)

# 以追加模式打开文件。文件不存在则创建，存在则从末尾写入。
with open("data/example_output_text.dat","a") as f:
    f.writelines(output_list)


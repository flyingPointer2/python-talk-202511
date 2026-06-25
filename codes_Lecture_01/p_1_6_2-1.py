# with open as 读写文件示例1

# 读文件
with open("data/example_text.dat") as f:
    content = f.read()

with open("data/example_text.dat") as f:
    lines = f.readlines()

print(content)
print(lines)

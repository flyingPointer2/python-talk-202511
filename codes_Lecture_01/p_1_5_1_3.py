# 错误的缩进示例
# NOTE 运行本脚本文件会报错（IndentationError）

year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "年是闰年")
else:
print(year, "年不是闰年")

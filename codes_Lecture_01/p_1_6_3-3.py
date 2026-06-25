# 输出格式控制示例

n = 7

# f-strings方法(Python >= 3.6)示例
print(f"10/{n:d} = {10/n:10.2f}".format(n,10/n))    # 保留2位小数 宽度为10
print(f"10/{n:d} = {10/n:10.2e}".format(n,10/n))    # 保留2位小数的科学计数法 宽度为10


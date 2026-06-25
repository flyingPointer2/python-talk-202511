# 比较列表推导式与显式for循环的效率

# NOTE timeit是Python自带的模块 可用于测试小段代码的执行速度
import timeit

# 显式for循环测试示例
loop_code = """
squares = []
for x in range(1000):
    squares.append(x * x)
"""

# 列表推导式测试示例
comprehension_code = "[x * x for x in range(1000)]"

# 测量执行时间 重复命令10000次取平均值
loop_time = timeit.timeit(stmt=loop_code, number=10000)
comprehension_time = timeit.timeit(stmt=comprehension_code, number=10000)

print("显式for循环用时是列表推导式用时的 " + str(loop_time/comprehension_time) + " 倍")

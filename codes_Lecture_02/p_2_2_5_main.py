# 接收函数对象作为函数参数示例

# 用二分法求解非线性方程示例

import math
from p_2_2_5_methods import bisection_method

def func(x):
    return math.exp(x) + x**3 + math.sin(x)

try:
    root_bisection = bisection_method(-5, 0, func)
    print(f"方程的根: {root_bisection:.3f}")
except ValueError as e:
    print(f"错误：{e}")



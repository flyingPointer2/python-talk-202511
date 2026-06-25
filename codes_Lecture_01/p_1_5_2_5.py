# while循环示例 牛顿法迭代求解一个正实数a的平方根

a = 2024

is_converged = False    # 标记是否收敛 初始值为False
x = a                   # 起始迭代值为a
max_error = 1e-8        # 计算收敛所允许的最大误差

# 当计算未收敛时 进行循环体内的迭代操作
while not is_converged: 
    x_new = (x + a/x) / 2
    if abs(x_new - x) < max_error:   # 若新值与旧值相差足够小 则计算收敛
        is_converged = True
    x = x_new


print(a, "的平方根是", x)

# 检验计算的收敛性
import math
print("计算值与标准值的偏差 = ", abs(math.sqrt(a)-x))




# while循环基本语法

# while 条件表达式:
#     循环体



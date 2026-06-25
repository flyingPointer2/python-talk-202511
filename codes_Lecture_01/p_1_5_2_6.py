# break示例 牛顿法迭代求解正实数a的算术平方根

a = 2026

x = a                   # 起始迭代值为a
max_error = 1e-8        # 计算收敛所允许的最大误差

# 持续迭代 直到循环体内触发break命令
while True: 
    x_new = (x + a/x) / 2
    if abs(x_new - x) < max_error:   # 若新值与旧值相差足够小 则计算收敛
        x = x_new
        break
    x = x_new

print(a, "的平方根是", x)

# 检验计算的收敛性
import math
print("计算值与标准值的偏差 = ", abs(math.sqrt(a)-x))

# 选择结构示例2

example_number = 2024
condition_1 = example_number%8 == 0
condition_2 = example_number%4 == 0

if condition_1:
    print("条件1满足！")
    print("执行操作1")
elif condition_2:
    print("条件1不满足，但条件2满足！")
    print("执行操作2")
else:
    print("条件1、条件2都不满足！")
    print("执行操作3")

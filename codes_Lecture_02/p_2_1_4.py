# 异常处理示例3

# 模拟理想竖直上抛运动 求t=1时刻的速度（向上为正方向）
# 通过输入文件读取初速度数据，若文件未找到，则使用默认值。

try:
    with open("initial_speed.dat","r") as f:
        input_data_str = f.read()
except FileNotFoundError:
    print("未找到输入文件，初始速度使用默认值")
    v0 = 10.0
else:
    v0 = float(input_data_str)

g = 9.8
t = 1.0
v = v0 - g * t

print(f"初始速度 = {v0:.3f}")
print(f"当 t = 1 时，速度 = {v:.3f}")

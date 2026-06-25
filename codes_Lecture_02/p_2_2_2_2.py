# 参数传递示例2 默认值参数示例

def cylinder_volume(r, h=1):
    """ 计算圆柱的体积 """
    pi = 3.14159
    volume = pi * r**2 * h
    return volume


print(cylinder_volume(3))
print(cylinder_volume(3, 4))



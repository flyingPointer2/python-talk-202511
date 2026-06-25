# 函数定义与调用示例

def triangle_area(a,b,c):
    """ 计算三角形的面积 """
    p = (a+b+c) / 2
    S = (p*(p-a)*(p-b)*(p-c))**(1/2)
    return S

line_lengths = [3,4,5]
area = triangle_area(line_lengths[0],line_lengths[1],line_lengths[2])
print(f"三角形的面积为{area}")


# doc_string 示例

# print(triangle_area.__doc__)
# print(print.__doc__)

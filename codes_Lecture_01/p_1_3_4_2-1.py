# 逻辑运算举例(1)


# 顺序：优先计算单个条件，然后逻辑运算（与或非），最后赋值操作
#   （若记不清楚，可用括号强制规定优先运算顺序）
GPA = 3.99
conditional_test = (GPA > 3.90 and GPA < 3.95)
print("GPA是否大于3.90且小于3.95? ",conditional_test) # False


# 接收函数对象作为函数参数示例

# 通用的二分法求解非线性方程


def bisection_method(a, b, f, tol=1e-8):
    """ 二分法求方程的根 """
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise ValueError("函数在两个端点 a 与 b 处的值符号相同！")
    
    while abs(b - a)/2 > tol:
        c = (a + b) / 2
        fc = f(c)

        if fc == 0:
            break
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2


    




""" 测试模块 本模块包含多个非线性方程求根函数 """
import math

def quadratic(a, b, c):
    """ 求解一元二次方程的复数根

    ax<sup>2</sup>+bx+c=0

    - a : 二次项系数
    - b : 一次项系数
    - c : 常数项
    """
    roots = [[0,0],[0,0]]
    if a == 0:
        raise ValueError("二次项系数 a 必须为非零！")
    
    delta = b*b-4.0*a*c
    if delta < 0:
        roots[1][0] = roots[0][0] = -b/(2*a)
        roots[0][1] = (-delta)**0.5 / (2*a)
        roots[1][1] = -roots[0][1]
    else:
        roots[0][0] = (-b+delta**0.5)/(2*a)
        roots[1][0] = (-b-delta**0.5)/(2*a)

    return roots


def cubic(a, b, c, d):
    """ 求解一元三次方程的根

    ax<sup>3</sup>+bx<sup>2</sup>+cx+d=0

    - a : 三次项系数
    - b : 二次项系数
    - c : 一次项系数
    - d : 常数项
    """
    roots = [[0,0],[0,0],[0,0]] # 存在3个复数根

    if a == 0:
        raise ValueError("三次项系数 a 必须为非零！")

    # 化为标准形式 x<sup>3</sup>+Ax<sup>2</sup>+Bx+C=0.
    A = b/a
    B = c/a
    C = d/a
    Q = (3*B-A**2)/9
    R = (9*A*B-27*C-2*A**3)/54
    D = Q**3+R**2

    # 所有根都是实根且至少两个根相等
    if D == 0:
        S = abs(R)**(1/3)
        roots[0][0] = -A/3+2*S
        roots[2][0] = roots[1][0] = -A/3-S
    # 一个实根，两个复数根
    elif D > 0:
        D = D**0.5
        S = abs(R+D)**(1/3)
        T = abs(R-D)**(1/3)
        roots[0][0] = -A/3+S+T
        roots[2][0] = roots[1][0] = -A/3-(S+T)/2
        roots[1][1] = 3**0.5*(S-T)/2
        roots[2][1] -= roots[1][1]
    # 三个复数根
    else:
        Q = -Q
        theta = math.acos(R/math.sqrt(Q**3))/3
        Q = 2*math.sqrt(Q)
        A = A/3
        roots[0][0] = Q*math.cos(theta)-A
        roots[1][0] = Q*math.cos(theta+2*math.pi/3)-A
        roots[2][0] = Q*math.cos(theta+4*math.pi/3)-A

    return roots


def bisection_method(f, a, b, tol=1e-8, max_iter=100):
    """ 二分法求方程的根

    - f : 待求零点的函数（即待求根的方程）
    - a : 估值区间的左端点
    - b : 估值区间的右端点
    - tol : 满足收敛条件的误差上限（即必须误差小于此值才能认为收敛）
    """
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise ValueError("函数在两个端点 a 与 b 处的值符号应当不相同！")
    
    k = 0
    while abs(b - a)/2 > tol:
        c = (a + b) / 2     # 区间中点
        fc = f(c)

        if fc == 0:
            break
        
        k += 1
        if k > max_iter:
            raise ValueError(f"迭代最大次数（{max_iter}次）但仍然不收敛！")
        
        # 更新区间的左右端点
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2



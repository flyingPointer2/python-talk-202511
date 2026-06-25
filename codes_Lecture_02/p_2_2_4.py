# 函数递归调用示例

def Fibnacci(n):
    """ 斐波那契数列的第n项(n >= 0) """
    if n == 0 or n == 1:
        return 1
    else:
        return Fibnacci(n-1) + Fibnacci(n-2)


# 输出斐波那契数列的前20项 
print([Fibnacci(x) for x in range(20)])

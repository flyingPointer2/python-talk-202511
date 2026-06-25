# import root_finding
# results = root_finding.cubic(1,0,0,-1)
# roots = [complex(result[0], result[1]) for result in results]
# print(roots)

# import root_finding as rf
# results = rf.cubic(1,0,0,-1)
# roots = [complex(result[0], result[1]) for result in results]
# print(roots)

from root_finding import bisection_method as bisect
result = bisect(lambda x:(-1+2*x**4+x**3), 0, 1)
print(f'函数的零点是：{result:.3f}')

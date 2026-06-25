# 列表的常用方法举例(4)

# 排序 示例2

ex1 = [1,2,4,1,-1,9,10,8]
print(sorted(ex1, reverse=True))    # 降序排序
print(sorted(ex1, reverse=False))   # 升序排序（默认选项）
print(sorted(ex1))

print('使用sorted排序后，原列表未改变：')
print(ex1)

ex1.sort()
print('使用sort排序后，原列表改变：')
print(ex1)

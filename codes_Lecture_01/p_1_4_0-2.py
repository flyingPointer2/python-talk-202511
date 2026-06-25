# 列表与字典的定义(2)


students_grades = {
    2024011001: 'A',
    2024011002: 'A-',
    2024011003: 'B',
    2024011004: 'A-',
}

# 通过键或get()方法来访问与该键相关联的值
print(students_grades[2024011002])
print(students_grades.get(2024011002))


# 错误代码示例：
# print(students_grades[2024011000])  # KeyError: 2024011000

# 【非错误代码】
# 若用 get() 方法获取不存在的键所对应的值，则返回 None
# print(students_grades.get(2024011000))    # None

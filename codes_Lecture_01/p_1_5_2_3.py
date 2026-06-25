# for循环示例3 遍历字典

students_grades = {
    2024011001: 'A',
    2024011002: 'A-',
    2024011003: 'B'
}

# 遍历字典的键（在本例中，字典的键表示学生的学号）
for student_id in students_grades.keys():
    print("Student's ID = " + str(student_id))

# 遍历字典的值（在本例中，字典的值表示学生的成绩（等级制））
for student_grade in students_grades.values():
    print("Student's grade = " + str(student_grade))

# 遍历字典的键值对
for stu_id, stu_grade in students_grades.items():
    print("Student's ID = " + str(stu_id) + ", grade = " + str(stu_grade))

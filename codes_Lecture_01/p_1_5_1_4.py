# 选择结构示例3 计算课程绩点

grade = 'A-'

# 方法1 通过选择结构计算绩点
if (grade in ['A+','A','A-']):
    score = 4.0
elif grade == 'B+':
    score = 3.6
elif grade == 'B':
    score = 3.3
elif grade == 'B-':
    score = 3.0
elif grade == 'C+':
    score = 2.6
elif grade == 'C':
    score = 2.3
elif grade == 'C-':
    score = 2.0
elif grade == 'D+':
    score = 1.6
elif grade == 'D':
    score = 1.3
else:
    score = 0

print("按照方法1计算，绩点 = ", score)

# 方法2 通过字典获取对应的绩点
GPA_dict = {
    'A+': 4.0,
    'A':4.0,
    'A-':4.0,
    'B+':3.6,
    'B':3.3,
    'B-':3.0,
    'C+':2.6,
    'C':2.3,
    'C-':2.0,
    'D+':1.6,
    'D':1.3,
    'F':0
}

score = GPA_dict.get(grade)
print("按照方法2计算，绩点 = ", score)

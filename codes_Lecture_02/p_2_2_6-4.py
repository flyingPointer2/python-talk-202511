# lambda 函数示例

# sorted()示例 学生按照成绩高低排序 

students = [
    {'Name':'Allen', 'score':99},
    {'Name':'Bob', 'score':89},
    {'Name':'Brent', 'score':90},
    {'Name':'Leib', 'score':75},
    {'Name':'Taylor', 'score':92},
    {'Name':'Lagrange', 'score':85},
    {'Name':'Bessel', 'score':61}
]

sorted_students = sorted(students, 
                        key=lambda x:x['score'], 
                        reverse=True
                    )

print(sorted_students)


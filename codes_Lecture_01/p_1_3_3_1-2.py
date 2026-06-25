# 在字符串中使用"+"和"*"运算符(2)

first_name = "Sherlock"

# NOTE：字符串不能直接和整数、浮点数通过"+"拼接
GPA = 3.999
message = first_name + ", your GPA is " + str(GPA)
# message = first_name + ", your GPA is " + GPA   # TypeError: can only concatenate str (not "float") to str
print(message)


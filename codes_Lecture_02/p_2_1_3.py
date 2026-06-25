# 常见异常类型举例

# 以下代码均处于注释的状态 取消注释即可获得对应的报错体验

# # (1) SyntaxError
# 2002年的第一场雪 = 2022


# # (2) NameError (假设变量name未定义)
# print(f"Hello, {name}")


# # (3) TypeError
# GPA = 3.99
# print("Your GPA is " + GPA)


# # (4) IndexError
# Fibonacci_list = [1,1,2,3,5,8]
# print(Fibonacci_list[len(Fibonacci_list)])


# # (5) KeyError
# student_info = {'name':'Sherlock', 'id':2024999666}
# print(f'学生成绩是{student_info["GPA"]}')


# # (6) ValueError
# user_input = '1oo'
# user_input_number = float(user_input)

# names = ['喜羊羊', '懒羊羊', '美羊羊','沸羊羊']
# names.remove('灰太狼')


# # (7) ZeroDivisionError
# number = 0
# result = 1/number


# # (8) FileNotFoundError
# file_path = 'file_that_not_exist.txt'
# with open(file_path) as f:
#     contents = f.read()
# print(contents)

# 思考：若文件打开模式改为"w"，上述代码可否正确运行？
 

# # (9) AttributeError
# "1223".reverse()

# # 正确用法:
# original_list = [1,2,4,3]
# original_list.reverse()
# print(original_list)


# # (10) ModuleNotFoundError (edge_tts是第三方库 不在Python自带的标准库中)
# import edge_tts

# # 若要正常使用该模块 请先使用如下命令进行安装
# #     pip install edge-tts
# # 该模块的使用方法可参考文档 https://pypi.org/project/edge-tts/

# 标准输入&输出的重定向示例
'''
可直接运行此脚本文件，或在（当前目录所在）终端输入如下命令

python p_1_6_1-2.py < data/in.dat > data/out.dat

'''

# 程序作用：从标准输入获取两个正整数（输入时以空格分隔）
#   然后用辗转相除法计算其最大公约数
#   然后将计算结果进行标准输出

numbers = input()
number_list = numbers.split()

a = int(number_list[0])
b = int(number_list[1])

while b != 0:
    temp = a
    a = b
    b = temp % b
    # 上述三行命令可用一行命令等效替代： a, b = b, a % b

print(a)


# 异常处理示例2

while True:
    user_input = input("请输入一个正实数（输入'q'退出程序）：")
    if user_input == 'q':
        break
    try:
        number = float(user_input)
        print("1/{:.3f} is {:.3f}".format(number, 1/number))
    except ZeroDivisionError:
        print("错误！应该输入非零数字！")
    except ValueError:
        print("错误！应该输入数字！")

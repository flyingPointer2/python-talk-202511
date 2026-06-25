# 标准输入示例 猜数字游戏

the_right_number = 42

print("请猜一猜正确的数字是什么~（提示：是一个10000以内的正整数）")
while True:
    user_input = input("请输入一个整数： ")
    
    # NOTE input函数返回值为字符串类型 需转化为整数类型再进行比较
    user_input_number = int(user_input)
    
    if user_input_number > the_right_number:
        print("数字太大了！")
    elif user_input_number < the_right_number:
        print("数字太小了！")
    else:
        print("猜测正确！")
        break
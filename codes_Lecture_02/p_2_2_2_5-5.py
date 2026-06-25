# 参数传递示例5 顺序要求(5)

# NOTE 运行此脚本会抛出SyntaxError的错误
# 错误原因: 在定义时，任意数量关键字参数须放在最后

def test(**kwargs, another_variable):
    """ 测试函数 """
    print("Test.")


# 类的继承示例
# 父类：三角形；子类：直角三角形

class Triangle:
    """ 三角形 """
    def __init__(self, a = 3, b = 4, c = 5):
        """ 初始化函数接收三角形三边的长度 """
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        """ Helen公式 计算三角形面积 """
        p = (self.a + self.b + self.c) / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**(1/2)

    def calculate_angles(self):
        """ 余弦定理 计算三角形的三个内角的余弦 """
        cos_a = (self.b**2 + self.c**2 - self.a**2)/(2*self.b*self.c)
        cos_b = (self.a**2 + self.c**2 - self.b**2)/(2*self.a*self.c)
        cos_c = (self.b**2 + self.a**2 - self.c**2)/(2*self.b*self.a)
        return cos_a, cos_b, cos_c

    def print_info(self):
        """ 输出信息 """
        print("我是一个三角形（`Triangle`）！ ")


class RightTriangle(Triangle):
    """ 直角三角形 """
    # 重写初始化函数
    def __init__(self, a=4, b=5):
        """ 初始化函数只需接收两直角边的长度 """
        c = (a**2 + b**2)**(1/2)
        # Triangle.__init__(self, a, b, c)   # 也可以通过这行代码调用父类的初始化函数
        super().__init__(a, b, c)   # 调用父类（super class）的初始化函数
    
    # 重写父类的成员方法
    def print_info(self):          
        print("我是一个直角三角形（`RightTriangle`）！")


if __name__ == "__main__":
    rt = RightTriangle(12)  # 思考：实参12传递给a还是b？
    rt.print_info()
    print(f"a={rt.a}, b={rt.b}, c={rt.c}")
    print(f"Area = {rt.calculate_area()}")

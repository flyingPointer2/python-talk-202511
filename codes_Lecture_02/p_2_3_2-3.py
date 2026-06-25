# 类和对象的基本概念(3) 

# 删除self参数后怎样？
# NOTE 本程序运行会报错TypeError

class Cat:
    """ 猫 """
    def __init__(self,name,age,height,weight):
        """ 初始化函数 创建对象时自动执行 """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    # meow()函数体内实际上未使用任何成员变量
    #   但是函数列表中仍需要包含self参数
    #   否则无法通过Cat类的实例调用此函数
    def meow():
        """ 喵喵叫 """
        print("Meow~ ")
    
    def catch_mouse(self):
        """ 捉老鼠 """
        print(f"{self.name} has caught a mouse!")

    def eat(self):
        """ 吃饭 """
        self.weight += 1    # 体重增加了！
        print(f"{self.name}'s weight is now {self.weight}")


if __name__ == "__main__":
    cat = Cat("小黑", 10, 30, 20)
    cat.meow()  # 这行代码目前不能正确运行 TypeError: Cat.meow() takes 0 positional arguments but 1 was given



# 类和对象的基本概念(1) 类的定义

class Cat:
    """ 猫 """
    def __init__(self,name,age,height,weight):
        """ 初始化函数 创建对象时自动执行 """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def meow(self):
        """ 喵喵叫 """
        print(f"Meow~ I am a cat named {self.name}.")
    
    def catch_mouse(self):
        """ 捉老鼠 """
        print(f"{self.name} has caught a mouse!")

    def eat(self):
        """ 吃饭 """
        self.weight += 1    # 体重增加了！
        print(f"{self.name}'s weight is now {self.weight}")


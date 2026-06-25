# 类和对象的基本概念(2) 类的实例化

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

# “主函数”入口
if __name__ == "__main__":
    # 创建Cat类的实例
    cat = Cat("小黑", 10, 30, 20)

    # 访问成员变量和成员方法
    print(f"{cat.name}现在{cat.age}岁了")
    cat.meow()

    # cat

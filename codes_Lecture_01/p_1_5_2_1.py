# for循环示例1 遍历列表

names = ['喜羊羊', '美羊羊', '懒羊羊', '沸羊羊']
goat_in_threeBodyWorld = 0

for name in names:
    print("你好，" + name + "，欢迎来到三体世界！")
    goat_in_threeBodyWorld += 1

print("已经有" + str(goat_in_threeBodyWorld) + "只羊来到了三体世界！")

# for循环的基本语法如下

# for 元素 in 可迭代对象:
#     循环体


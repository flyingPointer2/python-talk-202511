# continue示例 输出100以内不可以被2、3或5整除的正整数

counter = 0

for number in range(100):
    if (number%2 == 0 or number%3 == 0 or number%5 == 0):
        continue
    print(number)
    counter += 1

print("100以内，共有 " +str(counter)+" 个正整数满足条件")


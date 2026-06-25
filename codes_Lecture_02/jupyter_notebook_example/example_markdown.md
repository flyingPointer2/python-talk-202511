# 一级标题
## 二级标题
### 三级标题

无序列表：
- 微积分
- 线性代数
- 物理

有序列表：
1. 把冰箱门打开
2. 把大象装进去
3. 把冰箱门带上

代码块（Python语言）
```python
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
```
其中，`input`函数接收标准输入。


插入图片示例：
![train](images/vscode-icon.png)

数学公式示例：
$$
\int_{0}^{x} \frac{1}{1+s^2} \mathrm{d}s = \arctan x
$$

引用块示例：
> 哲学家们只是用不同的方式解释世界，问题在于改变世界。

水平分割线：
---

注：若要在Pycharm中预览，点击右上角的“编辑器和预览”按钮即可；
若要在VSCode中预览，可安装插件`Markdown Preview Enhanced`。



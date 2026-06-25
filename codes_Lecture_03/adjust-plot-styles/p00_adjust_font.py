import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

plt.style.use('mplstyles/science.mplstyle')

# 设置字体
font_path = "font/NotoSansSC-Regular.otf"
font_manager.fontManager.addfont(font_path)
font_name  = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_name

# 数据准备
X = np.linspace(-10,10,1000)
T = [2.0, 3.0]
Y1,Y2 = X*np.exp(-X**2/(2*T[0])), X*np.exp(-X**2/(2*T[1]))

# 画图
plt.figure()    # 创建新的画布
plt.plot(X, Y1, label="T = {}".format(T[0]))
plt.plot(X, Y2, label="T = {}".format(T[1]))
plt.title(r"示例标题文字 $E=mc^2$")
plt.xlabel("X 轴标签文字 (A.U.)")
plt.ylabel("Y 轴标签文字 (A.U.)")
plt.legend()
plt.savefig('test_00.jpg', dpi=600, bbox_inches='tight')
plt.show()
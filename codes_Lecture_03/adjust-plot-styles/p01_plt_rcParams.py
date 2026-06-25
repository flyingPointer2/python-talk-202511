import numpy as np
import matplotlib.pyplot as plt

with open('rcParams_full.txt', 'w', encoding='utf-8') as f:
    for k,v in plt.rcParams.items():
        f.write('{}: {}\n'.format(k,v))

plt.rcParams['font.family'] = 'Times New Roman' # 字体样式
plt.rcParams['lines.linewidth'] = 2             # 线宽
plt.rcParams['axes.labelsize'] = 14             # 坐标轴标签字体大小
plt.rcParams['mathtext.fontset'] = 'stix'       # 数学公式字体

X = np.linspace(-10,10,1000)
T = [2.0, 3.0]
Y1,Y2 = X*np.exp(-X**2/(2*T[0])), X*np.exp(-X**2/(2*T[1]))

plt.figure()    # 创建新的画布
plt.plot(X, Y1, label="T = {}".format(T[0]))
plt.plot(X, Y2, label="T = {}".format(T[1]))
plt.title(r"Title $E=mc^2$")
plt.xlabel("Temperature")
plt.ylabel("function")
plt.legend()
plt.savefig('test_01.jpg', dpi=600, bbox_inches='tight')
plt.show()
import numpy as np
import matplotlib.pyplot as plt



X = np.linspace(-10,10,1000)
T = [2.0, 3.0]
Y1,Y2 = X*np.exp(-X**2/(2*T[0])), X*np.exp(-X**2/(2*T[1]))



def plot_with_style(style_name):
    plt.style.use(style_name)
    plt.figure(figsize=(6.5,4.5))    # 创建新的画布
    plt.plot(X, Y1, label="T = {}".format(T[0]))
    plt.plot(X, Y2, label="T = {}".format(T[1]))
    plt.title(r"Title $E=mc^2$")
    plt.xlabel("Temperature")
    plt.ylabel("function")
    plt.legend()
    plt.savefig('test_05_{}.jpg'.format(style_name), dpi=600, bbox_inches='tight')


for style_name in plt.style.available:
    plot_with_style(style_name)
    print("Finish " + style_name)
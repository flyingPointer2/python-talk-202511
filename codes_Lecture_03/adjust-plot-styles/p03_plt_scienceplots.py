import numpy as np
import matplotlib.pyplot as plt

# pip install SciencePlots
import scienceplots
plt.style.use('science')

X = np.linspace(-10,10,1000)
T = [2.0, 3.0]
Y1,Y2 = X*np.exp(-X**2/(2*T[0])), X*np.exp(-X**2/(2*T[1]))

plt.figure(figsize=(7,5))    # 创建新的画布
plt.plot(X, Y1, label="T = {}".format(T[0]))
plt.plot(X, Y2, label="T = {}".format(T[1]))
plt.title(r"Title $E=mc^2$")
plt.xlabel("Temperature")
plt.ylabel("function")
plt.legend()
plt.savefig('test_03.jpg', dpi=600, bbox_inches='tight')
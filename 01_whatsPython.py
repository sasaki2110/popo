# Pythonとは？
# import this
# 英語かい・・・・・

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")

x = [-0.03, 0.78, 2.07, 2.77, 4.10, 5.38, 5.99, 6.84, 8.12, 8.89, 9.43]
y = [0.88, 2.45, 2.43, 4.07, 5.49, 6.46, 7.02, 8.27, 8.70, 10.23, 10.65]

#for _, item in enumerate(zip(x, y)):
#    plt.plot(item[0], item[1], marker='.')
#plt.savefig("sin.png")

# 自前でごりごり書く例

def fit(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    x_centered = [item - x_mean for item in x]
    y_centered = [item - y_mean for item in y]

    xy = [item_x * item_y for item_x, item_y in zip(x_centered, y_centered)]
    xx = [item * item for item in x_centered]
    sum_xy = sum(xy)
    sum_xx = sum(xx)

    a = sum_xy / sum_xx
    b = y_mean - a * x_mean

    return (a, b)

print(fit(x, y))  # 出力：(1.0037317148789446, 1.1006562375889226)

# numpy でやる例

import numpy as np
print(np.polyfit(x, y, 1))  # 出力：[1.00373171 1.10065624]

# ２行かい・・・・・・

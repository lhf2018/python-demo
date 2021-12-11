import numpy as np
import matplotlib.pyplot as plt

G = 6.67


x1 = 300
y1 = 50
m1 = 15

x2 = -100
y2 = -200
m2 = 12

x3 = -100
y3 = 150
m3 = 8

list1_X = []
list1_Y = []
list2_X = []
list2_Y = []
list3_X = []
list3_Y = []

dis1_2 = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
dis1_3 = np.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
dis2_3 = np.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
# 三体的初始速度
v1_x = 0  # 绿色
v1_y = 0
v2_x = 0  # 红色
v2_y = 0
v3_x = 0  # 蓝色
v3_y = 0

t = 0.1

for i in range(1000000):
    # 计算物体1
    # 2作用于1的加速度
    a1_2 = G * m2 / (dis1_2 ** 2)
    a1_3 = G * m3 / (dis1_3 ** 2)
    a1_x = a1_2 * (x2 - x1) / dis1_2 + a1_3 * (x3 - x1) / dis1_3
    a1_y = a1_2 * (y2 - y1) / dis1_2 + a1_3 * (y3 - y1) / dis1_3
    v1_x = v1_x + a1_x * t  # 物体1的速度
    v1_y = v1_y + a1_y * t  # 物体1的速度
    x1 = x1 + v1_x * t
    y1 = y1 + v1_y * t
    list1_X.append(x1)
    list1_Y.append(y1)

    # 计算物体2
    a2_1 = G * m1 / (dis1_2 ** 2)
    a2_3 = G * m3 / (dis2_3 ** 2)
    a2_x = a2_1 * (x1 - x2) / dis1_2 + a2_3 * (x3 - x2) / dis2_3
    a2_y = a2_1 * (y1 - y2) / dis1_2 + a2_3 * (y3 - y2) / dis2_3
    v2_x = v2_x + a2_x * t  # 物体2的速度
    v2_y = v2_y + a2_y * t  # 物体2的速度
    x2 = x2 + v2_x * t
    y2 = y2 + v2_y * t
    list2_X.append(x2)
    list2_Y.append(y2)

    # 计算物体3
    a3_1 = G * m1 / (dis1_3 ** 2)
    a3_2 = G * m2 / (dis2_3 ** 2)
    a3_x = a3_1 * (x1 - x3) / dis1_3 + a3_2 * (x2 - x3) / dis2_3
    a3_y = a3_1 * (y1 - y3) / dis1_3 + a3_2 * (y2 - y3) / dis2_3
    v3_x = v3_x + a3_x * t  # 物体3的速度
    v3_y = v3_y + a3_y * t  # 物体3的速度
    x3 = x3 + v3_x * t
    y3 = y3 + v3_y * t
    list3_X.append(x3)
    list3_Y.append(y3)

plt.plot(list1_X,list1_Y,color="darkorange")
plt.plot(list2_X,list2_Y,color="darkgreen")
plt.plot(list3_X, list3_Y, color="deepskyblue")

plt.legend()
plt.show()

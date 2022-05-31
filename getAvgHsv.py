import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

import os
img = cv.imread('E:/81/P000122__1__0___0.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
H, S, V = cv.split(hsv)
# h = H.flatten()
# s = S.flatten()
# v = V.flatten()
h = np.unique(H)
s = np.unique(S)
v = np.unique(V)
# _h = np.argmax(np.bincount(H_))  # 平均亮度


# _s = np.argmax(np.bincount(S_))

print(h, s, v)


def parseOpencv2TrueSV(x):
	return x / 255 * 100

def parseOpencv2TrueH(x):
	return x * 2



fig = plt.figure()
#创建绘图区域
ax = plt.axes(projection='3d')
#构建xyz
# plt.rcParams['agg.path.chunksize']=10000
# z = np.linspace(0, 370, 1000)
# x = z * np.sin(20 * z)
# y = z * np.cos(20 * z)
# c = x + y
# x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# z = np.array([0, 18, 34, 52, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255])
# z = parseOpencv2True(z)
x = parseOpencv2TrueSV(s)[0:150]
y = parseOpencv2TrueSV(v)[0:150]
z = parseOpencv2TrueH(h)[0:150]
c = (x*x + y*y + z*z) ** 0.5
ax.scatter3D(x, y, z, c=c)

ax.set_xlabel('S')  # 设置x坐标轴
ax.set_ylabel('V')  # 设置y坐标轴
ax.set_zlabel('H')  # 设置z坐标轴

ax.set_title('HSV展示图', fontproperties="STSong")
plt.show()
# plt.savefig('./基础5.png', # ⽂件名：png、jpg、pdf
# dpi = 100, # 保存图⽚像素密度
# facecolor = 'violet', # 视图与边界之间颜⾊设置
# edgecolor = 'lightgreen', # 视图边界颜⾊设置
# bbox_inches = 'tight')# 保存图⽚完整

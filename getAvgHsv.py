import numpy as np
import cv2 as cv
import os
img = cv.imread('E:/datadata/90.png')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
H, S, V = cv.split(hsv)
H_ = H.ravel()[np.flatnonzero(H)]  # 亮度非零的值
_h = np.sum(H_) / len(H_)
# _h = np.argmax(np.bincount(H_))  # 平均亮度
S_ = S.ravel()[np.flatnonzero(S)]
_s = np.sum(S_) / len(S_)

# _s = np.argmax(np.bincount(S_))
V_ = V.ravel()[np.flatnonzero(V)]
_v = np.sum(V_) / len(V_)
print(_h, _s,_v)
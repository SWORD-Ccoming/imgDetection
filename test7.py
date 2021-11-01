import cv2
import numpy
import numpy as np
import random
path_1 = r'81DarkWaterNoise.png'

img_1 = cv2.imread(path_1)
dataHSV = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)
# B, G, R = cv2.split(dataHSV)
# B[B < 10] = 0
# G[G < 10] = 0
# R[R < 10] = 0
# data = cv2.merge([B, G, R])
# dataRGBFULL = cv2.cvtColor(data, cv2.COLOR_HSV2BGR)
dst = cv2.bilateralFilter(src=dataHSV, d=0, sigmaColor=100, sigmaSpace=15)
dataRGBFULL = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)
cv2.imwrite('dark81gauss.png', dataRGBFULL)
cv2.imshow("iamge", dataRGBFULL)
cv2.waitKey(0)
# print(data_1)



import cv2
from pylab import *



data = cv2.imread("testdilate3.png")
data = cv2.resize(data, (600, 600))
k = np.ones((7, 7), np.uint8)
k0 = np.ones((3, 3), np.uint8)
k1 = np.ones((3, 3), np.uint8)
k2 = np.ones((2, 2), np.uint8)
# dataClose = cv2.morphologyEx(data,cv2.MORPH_CLOSE, kernel=k, iterations=1)
# dataClose = cv2.morphologyEx(data, cv2.MORPH_OPEN, kernel=k0, iterations=1)
# #
# data = data - dataClose
# dataClose = cv2.morphologyEx(data,cv2.MORPH_CLOSE, kernel=k1, iterations=2)
# kernel_2 = np.ones((4, 4), dtype=np.uint8) # 卷积核变为4*4
dilate1 = cv2.dilate(data, k, iterations=1)
erosion = cv2.erode(dilate1, k0, iterations=5)
dilate2 = cv2.dilate(erosion, k1, iterations=3)
# dilate = cv2.dilate(erosion, k, 5)
# erosion = cv2.erode(data, k0, iterations=1)
# ss = np.hstack((data, dilate))
cv2.imshow("imgClose", dilate2)
cv2.imwrite("testdilate2.png", dilate2)
# result = cv2.morphologyEx(dilate2, cv2.MORPH_TOPHAT, k2, iterations=1)
# cv2.imshow('result', result)
# cv2.imwrite('result.png', result)
cv2.waitKey(0)
# cv2.imshow("img1", data)
# cv2.imwrite("test10051.jpg", data)
# cv2.waitKey(0)

import cv2
from pylab import *



data = cv2.imread("weatherImg1Liner.png")
k = np.ones((3, 3), np.uint8)
dataClose = cv2.morphologyEx(data,cv2.MORPH_CLOSE, kernel=k, iterations=2)
cv2.imshow("imgClose", dataClose)
cv2.imwrite("dataClose2.png", dataClose)
cv2.waitKey(0)


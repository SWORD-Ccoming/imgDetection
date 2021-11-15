import cv2
import numpy as np

img = cv2.imread("4.jpg", 0)  # 由于Canny只能处理灰度图，所以将读取的图像转成灰度图

img = cv2.GaussianBlur(img, (7, 7), 0)  # 用高斯平滑处理原图像降噪。若效果不好可调节高斯核大小

canny = cv2.Canny(img, 0, 5)  # 调用Canny函数，指定最大和最小阈值，其中apertureSize默认为3。

cv2.imwrite('4canny.png', canny)
cv2.imshow('img', canny)

cv2.waitKey(0)

cv2.destroyAllWindows()
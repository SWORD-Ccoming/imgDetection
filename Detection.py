import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



def getAveHSV(imgFile = 'test1020.png'):
    img = cv2.imread(imgFile)
    img1 = cv2.imread('test1020.png')
    # hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imwrite('temp.png', img)#//中间过程
    gray = cv.imread('temp.png', cv.IMREAD_GRAYSCALE)
    contours, hierarchy = cv.findContours(image=gray, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
    areaList = []
    for i, cnt in enumerate(contours):
        rect = cv.minAreaRect(cnt)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        # (x, y, w, h) = rect
        # box = [x, y, w, h]
        area = cv.contourArea(cnt)
        if (area >0):
            cv2.drawContours(img1, [box], 0, (255, 255, 255), 1)
            # plt.imshow(img)
            # plt.show()

            areaList.append(area)
    plt.imshow(img1)
    plt.show()
    cv2.imwrite('2Detection.png', img1)
    return areaList
areaList = []
areaList = getAveHSV()
print(areaList, len(areaList))
import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def getAveHSV(imgFile = '1Canny.png'):
    img = cv2.imread(imgFile)
    img1 = cv2.imread('1.png')
    # hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imwrite('temp.png', img)#//中间过程
    gray = cv.imread('temp.png', cv.IMREAD_GRAYSCALE)
    contours, hierarchy = cv.findContours(image=gray, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
    areaList = []
    for i, cnt in enumerate(contours):
        rect = cv.boundingRect(cnt)
        (x, y, w, h) = rect
        box = [x, y, w, h]
        area = cv.contourArea(cnt)

        if ( area >0):
            cv.rectangle(img1, pt1=(x, y), pt2=(x + w, y + h), color=(0,  0, 0), thickness=2)
            # plt.imshow(img)
            # plt.show()
            areaList.append(area)
    plt.imshow(img1)
    plt.show()
    cv2.imwrite('320colorDetection.png', img1)
    return areaList
areaList = []
areaList = getAveHSV()
print(areaList, len(areaList))
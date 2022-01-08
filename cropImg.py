import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def getAveHSV(imgFile = "1015testnew.png"):
    img = cv2.imread(imgFile)
    img1 = cv2.imread("1015test.png")
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)
    cv.imwrite('temp.png', hsv)#//中间过程
    result = []#//当前图片的结果
    hResult = []
    sResult = []
    vResult = []
    gray = cv.imread('temp.png', cv.IMREAD_GRAYSCALE)
    contours, hierarchy = cv.findContours(image=gray, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
    for i, cnt in enumerate(contours):
        rect = cv.boundingRect(cnt)
        (x, y, w, h) = rect
        box = [x, y, w, h]
        area = cv.contourArea(cnt)
        if (area > 0):
            # cv.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 255, 255), thickness=3)
            # plt.imshow(img)
            # plt.show()
            crop_img = img1[y:y + h, x:x + w]
            writeImg(crop_img, i)
            # result.append([x, y, _H, _S, _V])
            # plt.imshow(crop_img)
            # plt.show()
            # return


def writeImg(crop_img, i):
    saveName = str(i) +'new'+'.png'
    cv.imwrite(saveName, crop_img)
getAveHSV()
import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os


def getHsv(img = None):
    dataHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    H, S, V = cv.split(dataHSV)
    # H_ = H.ravel()[np.flatnonzero(H)]
    # S_ = S.ravel()[np.flatnonzero(S)]
    # V_ = V.ravel()[np.flatnonzero(V)]
    return H, S, V


def getAveHSV(imgFile):
    img = cv2.imread(imgFile)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # h, s, v = cv.split(hsv)
    cv.imwrite('temp.png', hsv)#//中间过程
    gray = cv.imread('temp.png', cv.IMREAD_GRAYSCALE)
    contours, hierarchy = cv.findContours(image=gray, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
    for i, cnt in enumerate(contours):
        rect = cv.boundingRect(cnt)
        (x, y, w, h) = rect
        box = [x, y, w, h]
        area = cv.contourArea(cnt)

        if ( area > 1000):
            cv.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255,  255, 255), thickness=3)
            plt.imshow(img)
            plt.show()
            cropImg = img[y:y + h, x: x+h]
            _H, _S, _V = getHsv(cropImg)
    return _H, _S, _V


if __name__ == '__main__':
    path = 'E:/data2021'
    path_1 = 'E:/data2021'
    # recognitionRateList = []
    # f = open('recognitionRate.csv', 'w', encoding='utf-8')
    stringList = ['H', 'S', 'V']
    for filename in os.listdir(path):
        hsvList = []
        img_path = path + '/' + filename

        # data = cv2.imread(img_path)
        # dataHSV = cv2.cvtColor(data, cv2.COLOR_BGR2HSV)
        H, S, V = getAveHSV(img_path)
        hsvList.append(H)
        hsvList.append(S)
        hsvList.append(V)
        for i in range(3):
            # string = '' + i
            out_name = filename.split('.')[0] + stringList[i]
            save_name = path_1 + '/' + out_name + '.csv'
            np.savetxt(save_name, hsvList[i], delimiter=',')
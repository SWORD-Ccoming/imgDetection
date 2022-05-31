#-*- coding:utf-8 -*-
import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def avehsv(img = None):
    try:
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        H, S, V = cv.split(hsv)
        H_ = H.ravel()[np.flatnonzero(H)]  # 亮度非零的值
        _h = H_ / len(H_)
        # _h = np.argmax(np.bincount(H_))  # 平均亮度
        S_ = S.ravel()[np.flatnonzero(S)]
        _s = S_ / len(S_)

        # _s = np.argmax(np.bincount(S_))
        V_ = V.ravel()[np.flatnonzero(V)]
        _v = V_ / len(V_)
        # _v = np.argmax(np.bincount(V_))
        return _h, _s, _v
    except BaseException as e:
        pass



def getAveHSV(imgFile = 'test1020.png'):
    img = cv2.imread(imgFile)
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
            cv.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 255, 255), thickness=3)
            plt.imshow(img)
            plt.show()
            crop_img = img[y:y + h, x:x + w]
            _H, _S, _V = avehsv(crop_img)
            result.append([x, y, _H, _S, _V])
            # plt.imshow(crop_img)
            # plt.show()
            # return


    result.sort(key=lambda x: (x[1], x[0]))
    for i, d in enumerate(result):
        hResult.append(d[2])
        sResult.append(d[3])
        vResult.append(d[4])
    h = np.array(hResult)
    s = np.array(sResult)
    v = np.array(vResult)
    print(h.shape, s.shape, v.shape)
    return h, s, v

a, b, c = getAveHSV()




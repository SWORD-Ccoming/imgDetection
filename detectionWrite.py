import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os


def dots4ToRec4(poly):
	"""
    求出poly四点的最小外接水平矩形
    @param poly: poly[4]  [x,y]
    @return: xmin,xmax,ymin,ymax
    """
	xmin, xmax, ymin, ymax = min(poly[0][0], min(poly[1][0], min(poly[2][0], poly[3][0]))), \
							 max(poly[0][0], max(poly[1][0], max(poly[2][0], poly[3][0]))), \
							 min(poly[0][1], min(poly[1][1], min(poly[2][1], poly[3][1]))), \
							 max(poly[0][1], max(poly[1][1], max(poly[2][1], poly[3][1])))
	return xmin, ymin, xmax, ymax


def getHsv(img = None):
    dataHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    H, S, V = cv.split(dataHSV)
    H_ = np.sum(H) / (H.shape[0] * H.shape[1])
    S_ = np.sum(S) / (S.shape[0] * S.shape[1])
    V_ = np.sum(V) / (V.shape[0] * V.shape[1])
    return H_, S_, V_


# def getAveHSV(imgFile):
#     img = cv2.imread(imgFile)
#     hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#     # h, s, v = cv.split(hsv)
#     cv.imwrite('temp.png', hsv)#//中间过程
#     gray = cv.imread('temp.png', cv.IMREAD_GRAYSCALE)
#     contours, hierarchy = cv.findContours(image=gray, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
#     for i, cnt in enumerate(contours):
#         rect = cv.boundingRect(cnt)
#         (x, y, w, h) = rect
#         box = [x, y, w, h]
#         area = cv.contourArea(cnt)
#
#         if ( area > 1000):
#             cv.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255,  255, 255), thickness=3)
#             plt.imshow(img)
#             plt.show()
#             cropImg = img[y:y + h, x: x+h]
#             _H, _S, _V = getHsv(cropImg)
#     return _H, _S, _V

def getAveHSV(imgFile, x, y, w, h):
    img = cv2.imread(imgFile)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # h, s, v = cv.split(hsv)
    cv.imwrite('temp.png', hsv)#//中间过程
    gray = cv.imread('temp.png', cv.IMREAD_GRAYSCALE)
    contours, hierarchy = cv.findContours(image=gray, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)



    cropImg = img[y:y + h, x: x+w]
    _H, _S, _V = getHsv(cropImg)
    return _H, _S, _V

if __name__ == '__main__':
    path = 'E:/biyesheji/1/photoall'
    pathTxt = 'E:/biyesheji/1/outputall'
    path_1 = 'E:/biyesheji/1/test'
    hList = []
    sList = []
    vList = []
    count = 1
    # recognitionRateList = []
    # f = open('recognitionRate.csv', 'w', encoding='utf-8')
    stringList = ['H', 'S', 'V']
    for filename in os.listdir(path):

        inputList = []
        img_path = path + '/' + filename
        txtFilename = filename.split('.')[0] + '.txt'
        fileTxt = open(pathTxt+'/'+txtFilename, 'r')
        while True:
            inputList = fileTxt.readline()
            if not inputList:
                break
            inputList = inputList.split(' ')
            if inputList[10] == 'number-8\n':
                continue
            print(count)
            count = count + 1
            x0, y0, x1, y1, x2, y2, x3, y3 = inputList[2], inputList[3], inputList[4], inputList[5], inputList[6], \
                                         inputList[7], inputList[8], inputList[9]
            poly = [(int(x0), int(y0)), (int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3))]
            xmin, ymin, xmax, ymax = dots4ToRec4(poly)
            w = int((xmax - xmin) / 3)
            h = int(ymax - ymin)
        # data = cv2.imread(img_path)
        # dataHSV = cv2.cvtColor(data, cv2.COLOR_BGR2HSV)
            H, S, V = getAveHSV(img_path, xmin + (2 * w), ymin, w, h)
            hList.append([int(H * 2), 0, 0])
            sList.append([0, int(S / 255 * 360), 0])
            vList.append([0, 0, int(V / 255 * 360)])
        out_nameList = ['h2', 's2', 'v2']
        fileTxt.close()
    save_name = path_1 + '/' + out_nameList[0] + '.csv'
    np.savetxt(save_name, hList, delimiter=',')
    save_name = path_1 + '/' + out_nameList[1] + '.csv'
    np.savetxt(save_name, sList, delimiter=',')
    save_name = path_1 + '/' + out_nameList[2] + '.csv'
    np.savetxt(save_name, vList, delimiter=',')




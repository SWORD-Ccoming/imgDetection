import numpy
import numpy as np
import cv2
from sklearn.cluster import KMeans
import math
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
from sklearn import metrics
from sklearn.mixture import GaussianMixture
import os
import math
import csv
from GetAveHsv import getAveHSV

def scoreColorRecognition(raw_imgOrigin, raw_imgNew, k):
    dataHOriginArray, dataSOriginArray, dataVOriginArray = getAveHSV(raw_imgOrigin)
    dataHNewArray, dataSNewArray, dataVNewArray = getAveHSV(raw_imgNew)
    ofTheSameKindDifferList = []
    count = 0
    for i in range(k-1):
        dataHOrigin = int(dataHOriginArray[i])
        dataSOrigin = int(dataSOriginArray[i])
        dataVOrigin = int(dataVOriginArray[i])
        dataHNew = int(dataHNewArray[i])
        dataSNew = int(dataSNewArray[i])
        dataVNew = int(dataVNewArray[i])
        minHSV = ((dataHOrigin - dataHNew) * (dataHOrigin - dataHNew) + (dataSOrigin - dataSNew) * (dataSOrigin - dataSNew) + (dataVOrigin - dataVNew) * (dataVOrigin - dataVNew)) ** 0.5
        ofTheSameKindDifferList.append(minHSV)
    ofTheSameKindDifferArray = np.array(ofTheSameKindDifferList)
    booleanList = []
    for i in range(k-1):
        flag = True
        for j in range(k-1):
            dataHOrigin = int(dataHOriginArray[i])
            dataSOrigin = int(dataSOriginArray[i])
            dataVOrigin = int(dataVOriginArray[i])
            dataHNew = int(dataHNewArray[j])
            dataSNew = int(dataSNewArray[j])
            dataVNew = int(dataVNewArray[j])
            minHSV = ((dataHOrigin - dataHNew) * (dataHOrigin - dataHNew) + (dataSOrigin - dataSNew) * (
                        dataSOrigin - dataSNew) + (dataVOrigin - dataVNew) * (dataVOrigin - dataVNew)) ** 0.5
            if minHSV < ofTheSameKindDifferArray[i] and flag:
                flag = False
                break
        booleanList.append(flag)
    for i in range(k-1):
        if  booleanList[i] == True:
            count = count + 1
    return count/(k-1)


img_fileOrigin = r'81choose.png'
imgOrigin = Image.open(img_fileOrigin)
img_fileNew = r'81choosePhone7.jpg'
imgNew = Image.open(img_fileNew)
print(scoreColorRecognition(img_fileOrigin, img_fileNew, 82))
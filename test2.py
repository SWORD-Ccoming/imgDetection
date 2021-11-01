import numpy as np
import cv2
from sklearn.cluster import KMeans
import math
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
from sklearn import metrics
# 处理前(271,578) 处理后(212,40)
data = cv2.imread('1.png')
dataHSV = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', dataHSV)
cv2.waitKey(0)
cv2.imwrite('1Gray.png', dataHSV)
# H, S, V = cv2.split(dataHSV)
# print(dataHSV)

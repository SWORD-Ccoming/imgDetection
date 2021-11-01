import numpy as np
import cv2
from sklearn.cluster import KMeans
import math
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
from sklearn import metrics
from sklearn.mixture import GaussianMixture


img_file = r'ipadL5(5)after.png'
img = cv2.imread(img_file)
dataH1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
dataH, dataS, dataV = cv2.split(dataH1)
dataH = dataH.reshape(-1, 1)
dataS = dataS.reshape(-1, 1)
dataV = dataV.reshape(-1, 1)
dataHHeadIndexList = []
dataHEndIndexList = []
dataHCenterIndexList = []
centerIndex = 0
for index in range(len(dataH) - 20):
	if dataH[index] > 0 and dataH[index-1] == 0 and dataH[index+1] > 0 and dataH[index+2]:
		dataHHeadIndexList.append(index)
	if dataH[index] > 0 and dataH[index+1] == 0 and dataH[index-1] > 0:
		dataHEndIndexList.append(index)
for index in range(len(dataHHeadIndexList)):
		centerIndex = int(((dataHEndIndexList[index] + dataHHeadIndexList[index]) / 2))
		dataHCenterIndexList.append(centerIndex)
print(dataHCenterIndexList)


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
# imgOrigin = cv2.imread("72choose.png")
# imgNew = cv2.imread("ipad5 (5).bmp")
# count = 0
# imgOrigin = cv2.cvtColor(imgOrigin, cv2.COLOR_BGR2GRAY)
# imgNew = cv2.cvtColor(imgNew, cv2.COLOR_BGR2GRAY)
# imgNew = cv2.resize(imgNew, (570,510))
# imgNewAfter = cv2.morphologyEx(imgNew, cv2.MORPH_OPEN, (3,3))
# imgNewAfter = cv2.morphologyEx(imgNew, cv2.MORPH_CLOSE, (3,3))
# cv2.imwrite('E:/pythonProject/ipadL10-72pickAfter.png', imgNewAfter)


# noiseData = imgNew - imgOrigin
#
# plt.hist(noiseData.ravel(), 256)
# plt.show()
# imgNew = cv2.cvtColor(imgNew, cv2.COLOR_GRAY2BGR)
# cv2.imshow('imgNew', imgNew)
# cv2.waitKey(0)
path = 'E:/ipadnew'
path_1 = 'E:/fnlm'
for filename in os.listdir(path):
    # if filename.endswith('.bmp'):  #代表结尾是bmp格式的
	img_path = path + '/' + filename
	img = cv2.imread(img_path)
	img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
	out_name = filename.split('.')[0]
	save_name = path_1 + '/' + out_name + '.png'
	cv2.imwrite(save_name,img)

# deNoiseImgNew = cv2.fastNlMeansDenoisingColored(imgNew, None, 10, 10, 7, 21)
# deNoiseImgNew = cv2.GaussianBlur(imgNew, (3,3), 0)
# deNoiseImgNew = cv2.cvtColor(deNoiseImgNew, cv2.COLOR_BGR2GRAY)
# deNoiseImgNew = cv2.resize(deNoiseImgNew, (570, 510))
# noiseData = deNoiseImgNew - imgOrigin
# plt.hist(noiseData.ravel(), 256)
# plt.show()
# imgOrigin = cv2.cvtColor(imgOrigin, cv2.COLOR_BGR2GRAY)
# deNoiseImgNew = cv2.cvtColor(deNoiseImgNew, cv2.COLOR_BGR2GRAY)
# deNoiseImgNew = cv2.resize(deNoiseImgNew, (570, 510))
# noiseData = deNoiseImgNew - imgOrigin
# count = np.sum(noiseData > 0)
# cv2.imwrite('E:/pythonProject/ipadL5(5)after.png', deNoiseImgNew)
# cv2.imshow('imgNew', deNoiseImgNew)
# cv2.waitKey(0)
# print(count)
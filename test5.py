
import cv2
import cv2 as cv
import numpy as np


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('testweather3.png')
cv.imshow('img1', img)
cv.waitKey(0)
dst = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
# data = cv.cvtColor(dst, cv.COLOR_BGR2RGB)
cv.imwrite('test1005-90noNoise.jpg', dst)
cv.imshow('img', dst)

cv.waitKey(0)
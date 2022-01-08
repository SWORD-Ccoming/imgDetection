import numpy as np
import cv2
import os

data = cv2.imread("1 (1).jpg")
R, G, B = cv2.split(data)
r = np.ravel(R)
g = np.ravel(G)
b = np.ravel(B)
rList = set(list(r))
gList = set(list(g))
bList = set(list(b))
print(rList)

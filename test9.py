import cv2
import numpy as np
dataBGR = cv2.imread('color.png')
dataRGB = cv2.cvtColor(dataBGR, cv2.COLOR_BGR2RGB)
R,G3,B = cv2.split(dataRGB)
print(R.max(), np.min(R))
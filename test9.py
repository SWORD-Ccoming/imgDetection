import cv2
import numpy as np
from PIL import Image
raw_img = Image.open('weatherImng1.jpg')
dataBGR = cv2.imread('weatherImng1.jpg')
dataRGB = cv2.cvtColor(dataBGR, cv2.COLOR_BGR2RGB)
R, G, B = cv2.split(dataRGB)
img_shape = (raw_img.size[1], raw_img.size[0], 3)
img = np.zeros(img_shape, dtype=np.unit8)

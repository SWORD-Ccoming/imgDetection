import numpy as np
import cv2
import os
inputPath = 'E:/4030OriginImage/img/3001'
path_1 = 'E:/0001new'
for filename in os.listdir(inputPath):
	hsvList = []
	img_path = inputPath + '/' + filename
	data = cv2.imread(img_path)
	data = cv2.cvtColor(data,cv2.COLOR_BGR2HSV)
	H, S, V = cv2.split(data)
	H[H == ]
	out_name = filename.split('.')[0]
	save_name = path_1 + '/' + out_name + '.png'
	cv2.imwrite(save_name, data)
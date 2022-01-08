import numpy as np
import cv2
import os
inputPath = 'E:/4030OriginImage/img/3001'
path_1 = 'E:/0001new'
for filename in os.listdir(inputPath):
	hsvList = []
	img_path = inputPath + '/' + filename
	data = cv2.imread(img_path)
	R, G, B = cv2.split(data)
	r = np.ravel(R)
	rList = set(list(r))
	if len(rList) > 3:
		out_name = filename.split('.')[0]
		save_name = path_1 + '/' + out_name + '.png'
		cv2.imwrite(save_name, data)


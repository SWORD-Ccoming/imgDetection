import numpy as np
import cv2
import os
path = 'E:/1001'
path_1 = 'E:/0001new'
# recognitionRateList = []
# f = open('recognitionRate.csv', 'w', encoding='utf-8')
# stringList = ['H', 'S', 'V']
for filename in os.listdir(path):
	hsvList = []
	img_path = path + '/' + filename
	data = cv2.imread(img_path)
	# gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
	R, G, B = cv2.split(data)
	# hsvList.append(H)
	# hsvList.append(S)
	# hsvList.append(V)
	r = np.ravel(R)
	rList = set(list(r))
	if len(rList) > 2:
		out_name = filename.split('.')[0]
		save_name = path_1 + '/' + out_name + '.png'
		cv2.imwrite(save_name, data)
	# string = '' + i


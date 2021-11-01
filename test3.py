import numpy as np
import cv2
import os
path = 'E:/datahsv'
path_1 = 'E:/datahsv'
# recognitionRateList = []
# f = open('recognitionRate.csv', 'w', encoding='utf-8')
stringList = ['H', 'S', 'V']
for filename in os.listdir(path):
	hsvList = []
	img_path = path + '/' + filename
	data = cv2.imread(img_path)
	dataHSV = cv2.cvtColor(data, cv2.COLOR_BGR2HSV)
	H, S, V = cv2.split(dataHSV)
	hsvList.append(H)
	hsvList.append(S)
	hsvList.append(V)
	for i in range(3):
		# string = '' + i
		out_name = filename.split('.')[0] + stringList[i]
		save_name = path_1 + '/' + out_name + '.csv'
		np.savetxt(save_name, hsvList[i], delimiter=',')

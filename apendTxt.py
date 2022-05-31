import os

import cv2
import numpy as np
import xml.etree.ElementTree as ET
import math
import numpy as np

if __name__ == '__main__':
	classnames_v1_5 = ['number', 'number-8', 'number-##']
	k = 0
	# source_dir是存放.xml文件的文件夹
	source_dir = 'C:/Users/ROG/Downloads/detection (1)/test/newlabels/'
	# dst_dir是存放生成的文本文件的文件夹
	dst_dir = 'C:/Users/ROG/Desktop/colorDataSet/labels/'
	# dst_dir = 'E:/颜色图片数据集/860 703/labels/'
	# img = cv2.imread('C:/Users/ROG/Desktop/resultclass1/81.jpg')
	for file in os.listdir(source_dir):
		for fileJ in os.listdir(dst_dir):
			boxes_list = []
			inputList = []
			if(file == fileJ):
				fileObject = open(source_dir + file)
				line = fileObject.readlines()
				fileObjectJ = open(dst_dir + fileJ, 'a+')
				fileObjectJ.writelines(line)
				fileObject.close()
				fileObjectJ.close()
			# if(fileJ == file):
			# 	continue
			# else:
			# 	print(file)


import os

import cv2
import numpy as np
import xml.etree.ElementTree as ET
import math
import numpy as np

def rotatePoint(xc, yc, xp, yp, theta):
	xoff = xp - xc;
	yoff = yp - yc;
	cosTheta = math.cos(theta)
	sinTheta = math.sin(theta)
	pResx = cosTheta * xoff + sinTheta * yoff
	pResy = - sinTheta * xoff + cosTheta * yoff
	return str(int(xc + pResx)), str(int(yc + pResy))


def dots4ToRec4(poly):
	"""
    求出poly四点的最小外接水平矩形
    @param poly: poly[4]  [x,y]
    @return: xmin,xmax,ymin,ymax
    """
	xmin, xmax, ymin, ymax = min(poly[0][0], min(poly[1][0], min(poly[2][0], poly[3][0]))), \
							 max(poly[0][0], max(poly[1][0], max(poly[2][0], poly[3][0]))), \
							 min(poly[0][1], min(poly[1][1], min(poly[2][1], poly[3][1]))), \
							 max(poly[0][1], max(poly[1][1], max(poly[2][1], poly[3][1])))
	return xmin, ymin, xmax, ymax


def dots4ToRecC(poly, img_w, img_h):
	"""
    求poly四点坐标的最小外接水平矩形,并返回yolo格式的矩形框表现形式xywh_center(归一化)
    @param poly: poly – poly[4] [x,y]
    @param img_w: 对应图像的width
    @param img_h: 对应图像的height
    @return: x_center,y_center,w,h(均归一化)
    """
	xmin, ymin, xmax, ymax = dots4ToRec4(poly)
	x = (xmin + xmax) / 2
	y = (ymin + ymax) / 2
	w = xmax - xmin
	h = ymax - ymin
	return x / img_w, y / img_h, w / img_w, h / img_h


# file = open(dirName)
# inputList = file.readline().split(' ')
#
# x0, y0, x1, y1, x2, y2, x3, y3 = inputList[2], inputList[3], inputList[4], inputList[5], inputList[6], inputList[7], \
# 								 inputList[8], inputList[9]
# print(x0, y0, x1, y1, x2, y2, x3, y3, inputList)

if __name__ == '__main__':
	classnames_v1_5 = ['number', 'number-8', 'number-##']
	k = 0
	# source_dir是存放.xml文件的文件夹
	source_dir = 'C:/Users/ROG/Downloads/detection (1)/test/839860/'
	# dst_dir是存放生成的文本文件的文件夹
	dst_dir = 'C:/Users/ROG/Downloads/detection (1)/test/newlabels/'
	# img = cv2.imread('C:/Users/ROG/Desktop/resultclass1/81.jpg')
	for file in os.listdir(source_dir):
		boxes_list = []
		inputList = []
		fileTxt = open(source_dir + file, 'r')
		while True:

			inputList = fileTxt.readline()
			if not inputList:
				break
			inputList = inputList.split(' ')
			x0, y0, x1, y1, x2, y2, x3, y3 = inputList[2], inputList[3], inputList[4], inputList[5], inputList[6],inputList[7], inputList[8], inputList[9]
			print(x0, y0, x1, y1, x2, y2, x3, y3, inputList)
			poly = [(int(x0), int(y0)), (int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3))]

			angle = float(np.deg2rad(float(inputList[11].split('\n')[0])))
			print(angle)
			# points_array = np.array(poly).reshape(-1, 1, 2)
			# imgnew = cv2.drawContours(image=img,
			#                  contours=points_array,
			#                  contourIdx=-1,
			#                  color=(0, 255, 0),
			#                  thickness=2
			#                  )
			bbox = np.array(dots4ToRecC(poly, 839, 860))
			if bbox[2] < bbox[3]:
				tmp = bbox[2]
				bbox[2] = bbox[3]
				bbox[3] = tmp
				if angle < 1.570796:
					angle = angle + 1.570796
				else:
					angle = angle - 1.570796
			# 同样，angle应该也要在第一种情况的基础上减去一个pi/2
			# if angle < 1.57:
			#     theta = round(angle - np.pi*0.5, 6)
			# else:
			#     theta = round(angle - np.pi*1.5, 6)
			angle = math.degrees(angle)
			lines = str(classnames_v1_5.index(str(inputList[10]))) + ' ' + str(bbox[0]) + ' ' + str(
				bbox[1]) + ' ' + str(
				bbox[2]) + ' ' + str(bbox[3]) + ' ' + str(int(angle)) + '\n'
			boxes_list.append(lines)
		fileTxt.close()
		tmp = file.split(sep='.')
		# gt_name = dst_dir + 'P000' + tmp[0] + '__1__0___0' + '.txt'
		gt_name = dst_dir + tmp[0] + '.txt'
		gt_file = open(gt_name, 'w')
		gt_file.writelines(boxes_list)
		gt_file.close()

import cv2
import cv2 as cv
import numpy as np
# H(min, max) = (2.34, 138.6)
# S(min, max) = (109.9, 235.875)
# V(min, max) = (40, 100)

def create_image():
	imgH = np.zeros([30, 30], np.uint8)
	imgS = np.zeros([30, 30], np.uint8)
	imgV = np.zeros([30, 30], np.uint8)
	for i in range(0, 30):
		for j in range(0, 30):
			# if (j in range(0, 30) or j in range(60, 90) or j in range(150, 180) or j in range(210, 240) or j in range(270,300) or j in range(330,360) or j in range(390,420) or j in range(450,480) or j in range(510,540) ) and (i in range(0,30) or i in range(60,90) or i in range(150,180) or i in range(210,240) or i in range(270,300) or i in range(330,360) or i in range(390,420) or i in range(450,480) or i in range(510, 540) or i in range(570,600) or i in range(630,660) or i in range(690,720)):
				if j in range(0, 30):
					imgH[i,j] = 50
				# elif j in range(60, 90):
				# 	imgH[i,j] = 150
				# elif i in range(90,120):
				# 	imgH[i,j] = 18
				# elif i in range(150,180):
				# 	imgH[i,j] = 30
				# elif i in range(210,240):
				# 	imgH[i,j] = 40
				# elif i in range(270,300):
				# 	imgH[i,j] = 55
				# elif i in range(330,360):
				# 	imgH[i,j] = 70
				# elif i in range(390,420):
				# 	imgH[i,j] = 88
				# elif i in range(450,480):
				# 	imgH[i,j] = 112
				# elif i in range(510, 540):
				# 	imgH[i,j] = 135
				# elif i in range(570,600):
				# 	imgH[i,j] = 155
				# elif i in range(630,660):
				# 	imgH[i,j] = 175

	for i in range(0, 30):
		for j in range(0, 30):
			# if (j in range(30, 60) or j in range(90, 120) or j in range(150, 180) or j in range(210, 240) or j in range(270,300) or j in range(330,360) or j in range(390,420) or j in range(450,480) or j in range(510,540) ) and (i in range(30,60) or i in range(90,120) or i in range(150,180) or i in range(210,240) or i in range(270,300) or i in range(330,360) or i in range(390,420) or i in range(450,480) or i in range(510,540) or i in range(570,600) or i in range(630,660) or i in range(690,720)):
				if j in range(0,30) or j in range(60,90):
					imgS[i,j] = 255
				# elif j in range(90,120):
				# 	imgS[i,j] = 84
				# elif j in range(150,180):
				# 	imgS[i,j] = 108
				# elif j in range(210,240):
				# 	imgS[i,j] = 132
				# elif j in range(270,300):
				# 	imgS[i,j] = 156
				# elif j in range(330,360):
				# 	imgS[i,j] = 180
				# elif j in range(390,420):
				# 	imgS[i,j] = 204
				# elif j in range(450,480):
				# 	imgS[i,j] = 228
				# elif j in range(510,540):
				# 	imgS[i,j] = 252
	for i in range(0, 30):
		for j in range(0, 30):
			# if (j in range(30, 60) or j in range(90, 120) or j in range(150, 180) or j in range(210, 240) or j in range(270,300) or j in range(330,360) or j in range(390,420) or j in range(450,480) or j in range(510,540) ) and (i in range(30,60) or i in range(90,120) or i in range(150,180) or i in range(210,240) or i in range(270,300) or i in range(330,360) or i in range(390,420) or i in range(450,480) or i in range(510,540) or i in range(570,600) or i in range(630,660) or i in range(690,720)):
				if j in range(0,30):
					imgV[i,j] = 255
				# elif j in range(90,120) or j in range(270,300) or j in range(450,480):
				# 	imgV[i,j] = 178
				# elif j in range(150,180) or j in range(330,360) or j in range(510,540):
				# 	imgV[i,j] = 229



	dataRGB = cv2.merge([imgH, imgS, imgV])
	dataRGBFull = cv2.cvtColor(dataRGB, cv2.COLOR_HSV2BGR)
	cv.imwrite('E:/pythonProject/green.png', dataRGBFull)
	cv.imshow("iamge", dataRGBFull)
	cv.waitKey(0)
create_image()


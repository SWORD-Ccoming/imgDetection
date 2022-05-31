import cv2
import numpy as np

imgH = np.zeros([1230, 990], np.uint8)
imgS = np.zeros([1230, 990], np.uint8)
imgV = np.zeros([1230, 990], np.uint8)

for i in range(0, 1230):
	for j in range(0, 990):
		if (j in range(30, 60) or j in range(90, 120) or j in range(150, 180) or j in range(210, 240) or j in range(270,300) or j in range(330, 360) or j in range(390, 420) or j in range(450, 480) or j in range(510, 540) or j in range(570, 600) or j in range(630, 660)
			or j in range(690,720) or j in range(750,780) or j in range(810, 840) or j in range(870, 900) or j in range(930, 960)) and (i in range(30, 60) or i in range(90, 120) or i in range(150, 180) or i in range(210, 240) or i in range(270, 300) or i in range(330, 360)
			or i in range(390, 420) or i in range(450, 480) or i in range(510,540) or i in range(570, 600) or i in range(630, 660) or i in range(690, 720) or i in range(750, 780) or i in range(810, 840) or i in range(870, 900) or i in range(930,960) or i in range(990, 1020)
			or i in range(1050,1080) or i in range(1110, 1140) or i in range(1170, 1200)):
				if i in range(30, 60):
					imgH[i, j] = 0
				elif i in range(90, 120):
					imgH[i, j] = 5
				elif i in range(150, 180):
					imgH[i, j] = 10
				elif i in range(210, 240):
					imgH[i, j] = 16
				elif i in range(270, 300):
					imgH[i, j] = 20
				elif i in range(330, 360):
					imgH[i, j] = 24
				elif i in range(390, 420):
					imgH[i, j] = 29
				elif i in range(450, 480):
					imgH[i, j] = 35
				elif i in range(510, 540):
					imgH[i, j] = 40
				elif i in range(570, 600):
					imgH[i, j] = 47
				elif i in range(630, 660):
					imgH[i, j] = 50
				elif i in range(690, 720):
					imgH[i, j] = 55
				elif i in range(750, 780):
					imgH[i, j] = 62
				elif i in range(810, 840):
					imgH[i, j] = 69
				elif i in range(870, 900):
					imgH[i, j] = 72
				elif i in range(930, 960):
					imgH[i, j] = 78
				elif i in range(990, 1020):
					imgH[i, j] = 80
				elif i in range(1050, 1080):
					imgH[i, j] = 90
				elif i in range(1110, 1140):
					imgH[i, j] = 91
				elif i in range(1170, 1200):
					imgH[i, j] = 100
for i in range(0, 1230):
	for j in range(0, 990):
		if (j in range(30, 60) or j in range(90, 120) or j in range(150, 180) or j in range(210, 240) or j in range(270,300) or j in range(330, 360) or j in range(390, 420) or j in range(450, 480) or j in range(510, 540) or j in range(570, 600) or j in range(630, 660)
			or j in range(690,720) or j in range(750,780) or j in range(810, 840) or j in range(870, 900) or j in range(930, 960)) and (i in range(30, 60) or i in range(90, 120) or i in range(150, 180) or i in range(210, 240) or i in range(270, 300) or i in range(330, 360)
			or i in range(390, 420) or i in range(450, 480) or i in range(510,540) or i in range(570, 600) or i in range(630, 660) or i in range(690, 720) or i in range(750, 780) or i in range(810, 840) or i in range(870, 900) or i in range(930,960) or i in range(990, 1020)
			or i in range(1050,1080) or i in range(1110, 1140) or i in range(1170, 1200)):
				if j in range(30, 60) or j in range(90, 120) or j in range(150, 180) or j in range(210, 240):
					imgS[i, j] = 179
				elif j in range(270,300) or j in range(330, 360) or j in range(390, 420) or j in range(450, 480):
					imgS[i, j] = 205
				elif j in range(510, 540) or j in range(570, 600) or j in range(630, 660) or j in range(690,720):
					imgS[i, j] = 230
				elif j in range(750,780) or j in range(810, 840) or j in range(870, 900) or j in range(930, 960):
					imgS[i, j] = 255
for i in range(0, 1230):
	for j in range(0, 990):
		if (j in range(30, 60) or j in range(90, 120) or j in range(150, 180) or j in range(210, 240) or j in range(270,300) or j in range(330, 360) or j in range(390, 420) or j in range(450, 480) or j in range(510, 540) or j in range(570, 600) or j in range(630, 660)
			or j in range(690,720) or j in range(750,780) or j in range(810, 840) or j in range(870, 900) or j in range(930, 960)) and (i in range(30, 60) or i in range(90, 120) or i in range(150, 180) or i in range(210, 240) or i in range(270, 300) or i in range(330, 360)
			or i in range(390, 420) or i in range(450, 480) or i in range(510,540) or i in range(570, 600) or i in range(630, 660) or i in range(690, 720) or i in range(750, 780) or i in range(810, 840) or i in range(870, 900) or i in range(930,960) or i in range(990, 1020)
			or i in range(1050,1080) or i in range(1110, 1140) or i in range(1170, 1200)):
				if (j in range(30, 60) or j in range(270, 300) or j in range(510, 540) or j in range(750, 780)) and (i in range(30, 60) or i in range(150, 180) or i in range(270,300) or i in range(390, 420) or i in range(510, 540) or i in range(630, 660) or i in range(750, 780) or i in range(870, 900)
				or i in range(990, 1020) or i in range(1110, 1140)):
					imgV[i, j] = 178
				elif (j in range(90, 120) or j in range(330, 360) or j in range(570, 600) or j in range(810, 840)) and (i in range(30, 60) or i in range(150, 180) or i in range(270,300) or i in range(390, 420) or i in range(510, 540) or i in range(630, 660) or i in range(750, 780) or i in range(870, 900)
				or i in range(990, 1020) or i in range(1110, 1140)):
					imgV[i, j] = 204
				elif (j in range(150, 180) or j in range(390, 420) or j in range(630, 660) or j in range(870, 900)) and (i in range(30, 60) or i in range(150, 180) or i in range(270,300) or i in range(390, 420) or i in range(510, 540) or i in range(630, 660) or i in range(750, 780) or i in range(870, 900)
				or i in range(990, 1020) or i in range(1110, 1140)):
					imgV[i, j] = 229
				elif(j in range(210, 240) or j in range(450, 480) or j in range(690, 720) or j in range(930, 960)) and (i in range(30, 60) or i in range(150, 180) or i in range(270,300) or i in range(390, 420) or i in range(510, 540) or i in range(630, 660) or i in range(750, 780) or i in range(870, 900)
				or i in range(990, 1020) or i in range(1110, 1140)):
					imgV[i, j] = 255
				elif (j in range(30, 60) or j in range(270, 300) or j in range(510, 540) or j in range(750, 780)) and (i in range(90, 120) or i in range(210, 240) or i in range(330, 360) or i in range(450, 480) or i in range(570, 600) or i in range(690, 720) or i in range(810, 840) or i in range(930, 960)
				or i in range(1050, 1080) or i in range(1170, 1200)):
					imgV[i, j] = 255
				elif (j in range(90, 120) or j in range(330, 360) or j in range(570, 600) or j in range(810, 840)) and (i in range(90, 120) or i in range(210, 240) or i in range(330, 360) or i in range(450, 480) or i in range(570, 600) or i in range(690, 720) or i in range(810, 840) or i in range(930, 960)
				or i in range(1050, 1080) or i in range(1170, 1200)):
					imgV[i, j] = 229
				elif (j in range(150, 180) or j in range(390, 420) or j in range(630, 660) or j in range(870, 900)) and (i in range(90, 120) or i in range(210, 240) or i in range(330, 360) or i in range(450, 480) or i in range(570, 600) or i in range(690, 720) or i in range(810, 840) or i in range(930, 960)
				or i in range(1050, 1080) or i in range(1170, 1200)):
					imgV[i, j] = 204
				elif (j in range(210, 240) or j in range(450, 480) or j in range(690, 720) or j in range(930, 960)) and (i in range(90, 120) or i in range(210, 240) or i in range(330, 360) or i in range(450, 480) or i in range(570, 600) or i in range(690, 720) or i in range(810, 840) or i in range(930, 960)
				or i in range(1050, 1080) or i in range(1170, 1200)):
					imgV[i, j] = 178
dataRGB = cv2.merge([imgH, imgS, imgV])
out_nameList = ['h', 's', 'v']
path_1 = 'C:/Users/ROG/Desktop/test'
save_name = path_1 + '/' + out_nameList[0] + '.csv'
np.savetxt(save_name, np.unique(imgH), delimiter=',')
save_name = path_1 + '/' + out_nameList[1] + '.csv'
np.savetxt(save_name, np.unique(imgS), delimiter=',')
save_name = path_1 + '/' + out_nameList[2] + '.csv'
np.savetxt(save_name, np.unique(imgV), delimiter=',')
dataRGBFull = cv2.cvtColor(dataRGB, cv2.COLOR_HSV2BGR)
cv2.imwrite('E:/pythonProject/320color.png', dataRGBFull)
cv2.imshow("iamge", dataRGBFull)
cv2.waitKey(0)
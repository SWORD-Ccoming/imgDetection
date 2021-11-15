import cv2
import cv2 as cv
import imutils
import numpy as np
import matplotlib.pyplot as plt
import math
#逆时针旋转
def Nrotate(angle,valuex,valuey,pointx,pointy):
      angle = (angle/180)*math.pi
      valuex = np.array(valuex)
      valuey = np.array(valuey)
      nRotatex = (valuex-pointx)*math.cos(angle) - (valuey-pointy)*math.sin(angle) + pointx
      nRotatey = (valuex-pointx)*math.sin(angle) + (valuey-pointy)*math.cos(angle) + pointy
      return (nRotatex, nRotatey)


#顺时针旋转
def Srotate(angle,valuex,valuey,pointx,pointy):
      angle = (angle/180)*math.pi
      valuex = np.array(valuex)
      valuey = np.array(valuey)
      sRotatex = (valuex-pointx)*math.cos(angle) + (valuey-pointy)*math.sin(angle) + pointx
      sRotatey = (valuey-pointy)*math.cos(angle) - (valuex-pointx)*math.sin(angle) + pointy
      return (sRotatex,sRotatey)


#将四个点做映射
def rotatecordiate(angle,rectboxs,pointx,pointy):
      output = []
      for rectbox in rectboxs:
        if angle>0:
          output.append(Srotate(angle, rectbox[0], rectbox[1], pointx, pointy))
        else:
          output.append(Nrotate(-angle, rectbox[0], rectbox[1], pointx, pointy))
      return output


def imagecrop(image, box):
    xs = [x[1] for x in box]
    ys = [x[0] for x in box]
    print(xs, ys)
    print(min(xs), max(xs), min(ys), max(ys))
    cropimage = image[min(xs):max(xs), min(ys):max(ys)]
    print(cropimage.shape)
    cropimage = imutils.rotate_bound(cropimage, 90)
    cv2.imwrite('cropimage1.png', cropimage)
    return cropimage

rotateimg = cv2.imread('1black.png')
cv.imwrite('temp.png', rotateimg)#//中间过程
gray = cv.imread('temp.png', cv.IMREAD_GRAYSCALE)
contours, hierarchy = cv.findContours(image=gray, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(contours[1])
box_origin = cv2.boxPoints(rect)
M = cv2.getRotationMatrix2D(rect[0], rect[2], 1)
dst = cv2.warpAffine(rotateimg, M, (2*rotateimg.shape[0], 2*rotateimg.shape[1]))
box = rotatecordiate(rect[2], box_origin, rect[0][0], rect[0][1])
imagecrop(dst, np.int0(box))
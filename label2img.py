# -*- coding:utf-8 -*-
import cv2
from math import *
import numpy as np
import time,math
import os
import re

'''旋转图像并剪裁'''
def mkdir(path):
    '''
    创建指定的文件夹
    :param path: 文件夹路径，字符串格式
    :return: True(新建成功) or False(文件夹已存在，新建失败)
    '''
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
         # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

def rotate(
        img,  # 图片
        pt1, pt2, pt3, pt4, angle, i, count
):
    print(pt1, pt2, pt3, pt4)
    withRect = math.sqrt((pt4[0] - pt1[0]) ** 2 + (pt4[1] - pt1[1]) ** 2)  # 矩形框的宽度
    heightRect = math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
    print(withRect, heightRect)
    angle = acos((pt4[0] - pt1[0]) / withRect) * (180 / math.pi)  # 矩形框旋转角度
    print(angle)
    if pt4[1] > pt1[1]:
        print("顺时针旋转")
    else:
        print("逆时针旋转")
        angle = -angle

    height = img.shape[0]  # 原始图像高度
    width = img.shape[1]   # 原始图像宽度
    rotateMat = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)  # 按angle角度旋转图像
    heightNew = int(width * fabs(sin(radians(angle))) + height * fabs(cos(radians(angle))))
    widthNew = int(height * fabs(sin(radians(angle))) + width * fabs(cos(radians(angle))))

    rotateMat[0, 2] += (widthNew - width) / 2
    rotateMat[1, 2] += (heightNew - height) / 2
    imgRotation = cv2.warpAffine(img, rotateMat, (widthNew, heightNew), borderValue=(255, 255, 255))
    # cv2.imshow('rotateImg2',  imgRotation)
    # cv2.waitKey(0)

    # 旋转后图像的四点坐标
    [[pt1[0]], [pt1[1]]] = np.dot(rotateMat, np.array([[pt1[0]], [pt1[1]], [1]]))
    [[pt3[0]], [pt3[1]]] = np.dot(rotateMat, np.array([[pt3[0]], [pt3[1]], [1]]))
    [[pt2[0]], [pt2[1]]] = np.dot(rotateMat, np.array([[pt2[0]], [pt2[1]], [1]]))
    [[pt4[0]], [pt4[1]]] = np.dot(rotateMat, np.array([[pt4[0]], [pt4[1]], [1]]))

    # 处理反转的情况
    if pt2[1] > pt4[1]:
        pt2[1], pt4[1] = pt4[1], pt2[1]
    if pt1[0] > pt3[0]:
        pt1[0], pt3[0] = pt3[0], pt1[0]

    imgOut = imgRotation[int(pt2[1]):int(pt4[1]), int(pt1[0]):int(pt3[0])]
    # cv2.imshow("imgOut", imgOut)  # 裁减得到的旋转矩形框
    # cv2.waitKey(0)

    if imgOut.size != 0:
        cv2.imwrite('/Users/lidenghui/PycharmProjects/pythonlabelimage/result' + '/' + file.split('.')[0] + '/' + str(i) + '.png', imgOut)
    return imgRotation  # rotated image


# 根据四点画原矩形
def drawRect(img, pt1, pt2, pt3, pt4, color, lineWidth):
    cv2.line(img, pt1, pt2, color, lineWidth)
    cv2.line(img, pt2, pt3, color, lineWidth)
    cv2.line(img, pt3, pt4, color, lineWidth)
    cv2.line(img, pt1, pt4, color, lineWidth)


#　读出文件中的坐标值
def ReadTxt(directoryImage, directoryTxt, imageName, last, count):
    fileTxt = directoryTxt+'/'+last  # txt文件名
    getTxt = open(fileTxt, 'r')  # 打开txt文件
    lines = getTxt.readlines()
    i = 0
    for line in lines:
        x1 = int(list(line.split(' '))[2])
        y1 = int(list(line.split(' '))[3])
        x2 = int(list(line.split(' '))[4])
        y2 = int(list(line.split(' '))[5])
        x3 = int(list(line.split(' '))[6])
        y3 = int(list(line.split(' '))[7])
        x4 = int(list(line.split(' '))[8])
        y4 = int(list(line.split(' '))[9])
        angleStr = float(list(line.split(' '))[11][0:3])
        angle = int(angleStr)
        angle = radians(angle)
        pt1 = [x3, y3]
        pt2 = [x2, y2]
        pt3 = [x1, y1]
        pt4 = [x4, y4]
        xList = [x1, x2, x3, x4].sort() #从小到大排序
        yList = [y1, y2, y3, y4].sort()
        if angle in range(1, 90):
            if xList[0] == x1:
                pt1 = [x1, y1]
            elif xList[0] == x2:
                pt1 = [x2, y2]
            elif xList[0] == x3:
                pt1 = [x3, y3]
            elif xList[0] == x4:
                pt1 = [x4, y4]
            if xList[4] == x1:
                pt3 = [x1, y1]
            elif xList[4] == x2:
                pt3 = [x2, y2]
            elif xList[4] == x3:
                pt3 = [x3, y3]
            elif xList[4] == x4:
                pt3 = [x4, y4]
            if yList[0] == x1:
                pt4 = [x1, y1]
            elif yList[0] == x2:
                pt4 = [x2, y2]
            elif yList[0] == x3:
                pt4 = [x3, y3]
            elif yList[0] == x4:
                pt4 = [x4, y4]
            if yList[4] == x1:
                pt2 = [x1, y1]
            elif yList[4] == x2:
                pt2 = [x2, y2]
            elif yList[4] == x3:
                pt2 = [x3, y3]
            elif yList[4] == x4:
                pt2 = [x4, y4]
        elif angle in range(91, 180):
            if xList[0] == x1:
                pt2 = [x1, y1]
            elif xList[0] == x2:
                pt2 = [x2, y2]
            elif xList[0] == x3:
                pt2 = [x3, y3]
            elif xList[0] == x4:
                pt2 = [x4, y4]
            if xList[4] == x1:
                pt4 = [x1, y1]
            elif xList[4] == x2:
                pt4 = [x2, y2]
            elif xList[4] == x3:
                pt4 = [x3, y3]
            elif xList[4] == x4:
                pt4 = [x4, y4]
            if yList[0] == x1:
                pt1 = [x1, y1]
            elif yList[0] == x2:
                pt1 = [x2, y2]
            elif yList[0] == x3:
                pt1 = [x3, y3]
            elif yList[0] == x4:
                pt1 = [x4, y4]
            if yList[4] == x1:
                pt3 = [x1, y1]
            elif yList[4] == x2:
                pt3 = [x2, y2]
            elif yList[4] == x3:
                pt3 = [x3, y3]
            elif yList[4] == x4:
                pt3 = [x4, y4]
        # pt2 = list(map(float, line[i].split(' ')[:2]))
        # pt1 = list(map(float, line[i+1].split(' ')[:2]))
        # pt4 = list(map(float, line[i+2].split(' ')[:2]))
        # pt3 = list(map(float, re.split('\n|', line[i+3])[:2]))
        # # float转int
        #
        # pt2 = list(map(int, pt2))
        # pt1 = list(map(int, pt1))
        # pt4 = list(map(int, pt4))
        # pt3 = list(map(int, pt3))
        #
        imgSrc = cv2.imread(directoryImage+'/'+imageName)
        # drawRect(imgSrc, tuple(pt1), tuple(pt2), tuple(pt3), tuple(pt4), (0, 0, 255), 2)
        # cv2.imshow("img", imgSrc)
        cv2.waitKey(0)
        i += 1
        rotate(imgSrc, pt1, pt2, pt3, pt4, angle, i, count)


if __name__ == "__main__":
    count = 1
    # for i in range(1, 3):   # 遍历次数
    #     # if count == 6:
    #     #     count += 5
    #     # if count == 61:
    #     #     count += 20
    #     directory = "E:/test3"      #input 文件夹 存放图片和检测txt数据
    #     txtName = str(count) + '.txt'   #检测txt数据名字
    #     imageName = str(count) + '.png' #检测图片数据名字 和txtname需一一对应
    #     mkdir(directory + '/' + str(i))
    #     ReadTxt(directory, imageName, txtName, i)
    #     count += 1
    directoryImage = "C:/Users/ROG/Desktop/111/test4"  # input 文件夹 存放图片和检测txt数据
    # dst_dir是存放生成的文本文件的文件夹
    directoryTxt = "C:/Users/ROG/Desktop/111/test"
    # img = cv2.imread('C:/Users/ROG/Desktop/resultclass1/81.jpg')
    for file in os.listdir(directoryImage):
        if(file == '.DS_Store'):
            continue
        mkdir("C:/Users/ROG/Desktop/111/result" + '/' + file.split('.')[0])
        fileName = file.split('.')[0]
        fileName = fileName[0:8]
        ReadTxt(directoryImage ,directoryTxt, file, fileName + '.txt', count)
        count += 1
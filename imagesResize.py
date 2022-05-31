# -*- coding:utf-8 -*-
import cv2
import skimage
import os
import numpy as np


def add_noise_Guass(img, mean=0, var=0.01):  # 添加高斯噪声
    img = np.array(img / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, img.shape)
    out_img = img + noise
    if out_img.min() < 0:
        low_clip = -1
    else:
        low_clip = 0
        out_img = np.clip(out_img, low_clip, 1.0)
        out_img = np.uint8(out_img * 255)
    return out_img



if __name__ == "__main__":
    directoryImage = "E:/desktop/2020517dataset/traindatasetX2"  # input 文件夹 存放图片和检测txt数据
    directoryOutput = "E:/desktop/2020517dataset/test500"
    # dst_dir是存放生成的文本文件的文件夹
    # img = cv2.imread('C:/Users/ROG/Desktop/resultclass1/81.jpg')
    for file in os.listdir(directoryImage):
        image = cv2.imread(directoryImage + '/' + file)
        image = cv2.resize(image, (500, 500))
        print('处理结束{}'.format(file))
        cv2.imwrite(directoryOutput + '/' + file, image)
        # 以上代码为读取图片并进行resize
        # origin = skimage.io.imread(directoryImage + '/' + file)
        # nosiyImage = cv2.GaussianBlur(image, ksize=(3, 3,), sigmaX=0, sigmaY=0) #设定函数
        # cv2.imwrite(directoryOutput + '/' + file, nosiyImage)

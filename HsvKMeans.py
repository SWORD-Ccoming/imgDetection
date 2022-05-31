import numpy as np
import cv2
from sklearn.cluster import KMeans
import math
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from PIL import Image
from pylab import *
from sklearn import metrics
import os
import time


def color_cluster(img_file, k):
    img = cv2.imread(img_file)
    data = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # data = img
    data = data.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k).fit(data)
    # GMM = GaussianMixture(n_components=k).fit(data)
    pixel_label = kmeans.labels_            # 取出聚类中心
    # pixel_label = GMM.predict(data)
    # 计算聚类得分，Calinski-Harabasz分数值越大聚类结果越好
    # ch_score = metrics.calinski_harabasz_score(data, pixel_label)
    ch_score = 0
    # d_score = metrics.davies_bouldin_score(data, pixel_label)
    # print(ch_score, d_score)
    label_value = set(list(pixel_label))
    label_count = []
    hsv_avg = []
    for value in label_value:
        label_count.append(np.sum(pixel_label == value))
        hsv_mean = (np.sum(data[pixel_label == value], axis=0) / np.sum(pixel_label == value)).astype(np.uint8)
        hsv_avg.append(hsv_mean)
    hsv_array = np.reshape(np.array(hsv_avg), (k, 1, 3))
    rgb_array = cv2.cvtColor(hsv_array, cv2.COLOR_HSV2RGB)
    # rgb_array = hsv_array
    rgb_array = np.reshape(rgb_array, (k, 3))    # 101,3
    return np.array(list(label_value)), np.array(label_count), rgb_array, ch_score, pixel_label




def show2(raw_img, renders, start_k):
    mpl.rcParams['font.family'] = "SimHei"
    total_imgs = len(renders) + 1
    # 向上取整
    n_row = math.ceil(total_imgs / 4)
    # plt.subplot(1, 2, 1)
    # plt.title(u'原图')
    # plt.imshow(raw_img)
    plt.subplot(1, 2,  start_k)
    plt.title('聚类后')
    plt.imshow(render_img)
    plt.show()


def render(img_size, pixel_label, label_value, rgb_array, k, filename):
    # stringList = []
    # for i in range(k):
    #     num = i+1
    #     stringList.append(str(num))
    for i, value in enumerate(label_value):
        img_shape = (img_size[1], img_size[0], 3)
        img = np.zeros(img_shape, dtype=np.uint8)
        pixel_label = np.reshape(pixel_label, (img_size[1], img_size[0]))
        img[pixel_label == value] = rgb_array[i]
        render_img = Image.fromarray(img)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # if rgb_array[i][0] == 50 and rgb_array[i][1] == 11 and rgb_array[i][2]:
        save_name = filename + str(i)
        cv2.imwrite('E:/91/' + save_name+'.png', img)
    return render_img, img


if __name__ == '__main__':
    startTime = time.time()
    inputPath = 'E:/81'
    for filename in os.listdir(inputPath):
        img_path = inputPath + '/' + filename
        img_file = img_path
        max_score = -1000
        renders = []
        best_k = -1
        raw_img = Image.open(img_file)
        k = 4
        label_value, label_count, rgb_array, score, pixel_label = color_cluster(img_file, k)
        render_img, imgNew = render(raw_img.size, pixel_label, label_value, rgb_array, k, filename)
        renders.append(render_img)
    endTime = time.time()
    print(f"the running time is: {endTime - startTime} s")
    # show(label_value, label_count, rgb_array, k, raw_img, render_img)
    # if max_score < score:
    #     max_score = score
    #     best_k = k
    #     print(score)
    # show2(raw_img, renders, 2)
    #     plt.imshow(render_img)
    #     plt.show()
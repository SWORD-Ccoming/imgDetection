import numpy as np
import cv2
from sklearn.cluster import KMeans
import math
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
from sklearn import metrics
from sklearn.mixture import GaussianMixture
import os
import math
import csv
from ScoreColorRecoginition import scoreColorRecognition
def color_cluster(img_file, k):
    img = cv2.imread(img_file)
    data = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    data = data.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k).fit(data)
    # GMM = GMM = GaussianMixture(n_components=k).fit(data)
    pixel_label = kmeans.labels_
    clusterCenter = kmeans.cluster_centers_
    # pixel_label = GMM.predict(data)

    # clusterCenterH = clusterCenter[clusterCenter[:, 0].argsort()]
    # clusterCenterRow1 = clusterCenterH[1:10, :]
    # clusterCenterRow1 = clusterCenterRow1[clusterCenterRow1[:, 1].argsort()]
    label_value = set(list(pixel_label))
    label_count = []
    hsv_avg = []
    for value in label_value:
        label_count.append(np.sum(pixel_label == value))
        hsv_mean = (np.sum(data[pixel_label == value], axis=0) / np.sum(pixel_label == value)).astype(np.uint8)# 分子为与value同一个标签的像素点的和,分母为与value同一个标签的像素点的个数
        hsv_avg.append(hsv_mean)
    hsv_array = np.reshape(np.array(hsv_avg), (k, 1, 3))
    rgb_array = cv2.cvtColor(hsv_array, cv2.COLOR_HSV2RGB)
    rgb_array = np.reshape(rgb_array, (k, 3))    # 101,3
    return np.array(list(label_value)), np.array(label_count), rgb_array, pixel_label, clusterCenter


# def scoreColorRecognition(imgFileOrigin, imgFileNew, pixelLabelOrigin, pixelLabelNew, k, ImgOrigin, ImgNew):
#     centerIndexOrigin = []
#     centerIndexNew = []
#     rNewArray = []
#     gNewArray = []
#     bNewArray = []
#     rOriginArray = []
#     gOriginArray = []
#     bOriginArray = []
#     maxOrigin = 0
#     maxNew = 0
#     maxCountOrigin = 0
#     maxCountNew = 0
#     booleanArray = []
#     ofTheSameKindDifferList = []
#     minRGB = 0
#     count = 0
#     for i in range(k):
#         countOrigin = np.where(((pixelLabelOrigin) == i))
#         countOrigin = list(countOrigin)
#         if maxOrigin < len(countOrigin[0]):
#             maxOrigin = len(countOrigin[0])
#             maxCountOrigin = i
#         a = np.int64(countOrigin).sum()
#         b = np.max(countOrigin)
#         c = np.min(countOrigin)
#         d = (a-b-c)/((len(countOrigin[0])-2))
#         centerIndexOrigin.append(d)
#     for i in range(k):
#         countNew = np.where(np.array(pixelLabelNew) == i)
#         countNew = list(countNew)
#         if maxNew < len(countNew[0]):
#             maxNew = len(countNew[0])
#             maxCountNew = i
#         centerIndexNew.append((np.int64(countNew).sum()-np.int64(np.max(countNew))-np.int64(np.min(countNew)))/(np.int64(len(countNew[0])-2)))
#     centerIndexOrigin.pop(maxCountOrigin)
#     centerIndexNew.pop(maxCountNew)
#     centerIndexOrigin.sort()
#     centerIndexNew.sort()
#     dataImgOrigin = cv2.cvtColor(ImgOrigin, cv2.COLOR_BGR2HSV)
#     dataImgNew = cv2.cvtColor(ImgNew, cv2.COLOR_BGR2HSV)
#
#     rOrigin, gOrigin, bOrigin = cv2.split(dataImgOrigin)
#     rNew, gNew, bNew = cv2.split(dataImgNew)
#     rOrigin = rOrigin.reshape(-1, 1)
#     gOrigin = gOrigin.reshape(-1, 1)
#     bOrigin = bOrigin.reshape(-1, 1)
#     rNew = rNew.reshape(-1, 1)
#     gNew = gNew.reshape(-1, 1)
#     bNew = bNew.reshape(-1, 1)
#     # for i in range(k-1):
#     #     countOrigin.append(0)
#     #     indexNumberOrigin.append(0)
#     #     centerIndexOrigin.append(0)
#     #     countNew.append(0)
#     #     indexNumberNew.append(0)
#     #     centerIndexNew.append(0)
#     #     differList.append(0)
#     # for index in range(len(pixelLabelOrigin)):
#     #     for j in range(k):
#     #         if pixelLabelOrigin[index] == j:
#     #             countOrigin[j] = countOrigin[j] + index
#     #             indexNumberOrigin[j] =countOrigin[j] + 1
#     # countOrigin[indexNumberOrigin.index(max(indexNumberOrigin))]
#     # indexNumberOrigin.remove(max(indexNumberOrigin))
#     # for index in range(len(countOrigin)):
#     #     centerIndexOrigin[index] = int(countOrigin / indexNumberOrigin)
#     # centerIndexOrigin.sort()
#     # for index in range(len(pixelLabelNew)):
#     #     for j in range(k):
#     #         if pixelLabelNew[index] == j:
#     #             countNew[j] = countNew[j] + index
#     #             indexNumberNew[j] += 1
#     # countNew[indexNumberNew.index(max(indexNumberNew))]
#     # indexNumberNew.remove(max(indexNumberNew))
#     # for index in range(len(countNew)):
#     #     centerIndexNew[index] = int(countNew / indexNumberNew)
#     # centerIndexNew.sort()
#     for i in range(k-1):
#         ROrigin = int(rOrigin[int(centerIndexOrigin[i])])
#         GOrigin = int(gOrigin[int(centerIndexOrigin[i])])
#         BOrigin = int(bOrigin[int(centerIndexOrigin[i])])
#         RNew = int(rNew[int(centerIndexNew[i])])
#         GNew = int(gNew[int(centerIndexNew[i])])
#         BNew = int(bNew[int(centerIndexNew[i])])
#         # ROrigin = rOrigin[int(centerIndexOrigin[i] / imgFileOrigin[1]), int(centerIndexOrigin[i] % imgFileOrigin[1])]
#         # GOrigin = gOrigin[int(centerIndexOrigin[i] / imgFileOrigin[1]), int(centerIndexOrigin[i] % imgFileOrigin[1])]
#         # BOrigin = bOrigin[int(centerIndexOrigin[i] / imgFileOrigin[1]), int(centerIndexOrigin[i] % imgFileOrigin[1])]
#         # RNew = rNew[int(centerIndexNew[i] / imgFileNew[1]), int(centerIndexNew[i] % imgFileNew[1])]
#         # GNew = gNew[int(centerIndexNew[i] / imgFileNew[1]), int(centerIndexNew[i] % imgFileNew[1])]
#         # BNew = bNew[int(centerIndexNew[i] / imgFileNew[1]), int(centerIndexNew[i] % imgFileNew[1])]
#         RGBmindistance = ((ROrigin - RNew) * (ROrigin - RNew) + (BOrigin - BNew) * (BOrigin - BNew) + (GOrigin - GNew) * (GOrigin - GNew)) ** 0.5
#         rOriginArray.append(ROrigin)
#         gOriginArray.append(GOrigin)
#         bOriginArray.append(BOrigin)
#         rNewArray.append(RNew)
#         gNewArray.append(GNew)
#         bNewArray.append(BNew)
#         ofTheSameKindDifferList.append(RGBmindistance)
#
#     for j in range(k-1):
#         rOriginlast = int((rOriginArray[j]))
#         rNewlast = int((rNewArray[j]))
#         bOriginlast = int((bOriginArray[j]))
#         bNewlast = int((bNewArray[j]))
#         gOriginlast = int((gOriginArray[j]))
#         gNewlast = int((gNewArray[j]))
#         flag = True
#         minRGB = ((rOriginlast - rNewlast) * (rOriginlast - rNewlast) + (bOriginlast-bNewlast) * (bOriginlast-bNewlast) + (gOriginlast - gNewlast) * (gOriginlast - gNewlast)) ** 0.5
#         if minRGB > (ofTheSameKindDifferList[j]):
#             flag = False
#         booleanArray.append(flag)
#     for i in range(k-1):
#         if booleanArray[i] == True:
#             count = count + 1
#
#     return count/(k-1)


def show(raw_img, renders, start_k):
    mpl.rcParams['font.family'] = "SimHei"
    total_imgs = len(renders) + 1
    # 向上取整
    n_row = math.ceil(total_imgs / 4)
    plt.subplot(1, 2, 1)
    plt.title(u'原图')
    plt.imshow(raw_img)
    plt.subplot(1, 2,  start_k)
    plt.title('k = 101')
    plt.imshow(render_imgNew)
    plt.show()


def render(img_size, pixel_label, label_value, rgb_array):
    img_shape = (img_size[1], img_size[0], 3)
    img = np.zeros(img_shape, dtype=np.uint8)
    pixel_label = np.reshape(pixel_label, (img_size[1], img_size[0]))
    for i, value in enumerate(label_value):
        img[pixel_label == value] = rgb_array[i]
    # img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    render_img = Image.fromarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return render_img, img


if __name__ == '__main__':
    path = 'E:/81'
    path_1 = 'E:/81after'
    recognitionRateList = []
    f = open('recognitionRate.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(f)
    k = 82
    for filename in os.listdir(path):
        # if filename.endswith('.bmp'):  #代表结尾是bmp格式的
        img_path = path + '/' + filename
        # img = cv2.imread(img_path)
        img_fileNew = img_path
        raw_imgNew = Image.open(img_fileNew)
        img_fileOrigin = r'81.png'
        raw_imgOrigin = Image.open(img_fileOrigin)
        label_valueNew, label_countNew, rgb_arrayNew, pixel_labelNew, clusterCenterNew = color_cluster(img_fileNew, k)
        render_imgNew, imgNew = render(raw_imgNew.size, pixel_labelNew, label_valueNew, rgb_arrayNew)
        recognitionRateList.append(scoreColorRecognition(img_fileOrigin, img_fileNew , k))
        csv_writer.writerow(recognitionRateList)
        out_name = filename.split('.')[0]
        save_name = path_1 + '/' + out_name + '.png'
        cv2.imwrite(save_name, imgNew)

    # img_fileOrigin = r'72choose.png'
    # img_fileNew = r'ipadL5(5)after.png'
    # raw_imgOrigin = Image.open(img_fileOrigin)
    # raw_imgNew = Image.open(img_fileNew)
    # k = 82
    # differ = []
    # label_valueOrigin, label_countOrigin, rgb_arrayOrigin, pixel_labelOrigin = color_cluster(img_fileOrigin, k)
    # render_imgOrigin, imgOrigin = render(raw_imgOrigin.size, pixel_labelOrigin, label_valueOrigin ,rgb_arrayOrigin)
    # label_valueNew, label_countNew, rgb_arrayNew, pixel_labelNew = color_cluster(img_fileNew, k)
    # render_imgNew, imgNew = render(raw_imgNew.size, pixel_labelNew, label_valueNew, rgb_arrayNew)
    # differ = scoreColorRecognition(raw_imgOrigin.size, raw_imgNew.size, pixel_labelOrigin, pixel_labelNew, k, imgOrigin, imgNew)



    # show(label_value, label_count, rgb_array, k, raw_img, render_img)
    # show2(raw_img, renders, 2)
    # print(differ)
    # plt.imshow(render_imgNew)
    # plt.show()
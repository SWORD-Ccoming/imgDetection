import numpy as np
import cv2
from sklearn.cluster import KMeans
import math
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
from sklearn import metrics
UNCLASSIFIED = False
NOISE = -1


def __dis(vector1, vector2):
    """
    余弦夹角距离
    :param vector1: 向量A
    :param vector2: 向量B
    :return:
    """
    distance = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * (np.linalg.norm(vector2)))
    distance = max(0.0, 1.0 - float(distance))
    return distance


def __eps_neighborhood(vector1, vector2, eps):
    """
    是否邻居
    :param vector1: 向量A
    :param vector2: 向量B
    :param eps: 同一域下样本最大距离
    :return:
    """
    return __dis(vector1, vector2) < eps


def __region_query(data, point_id, eps):
    """
    核心函数，区域查询
    :param data: 数据集,array
    :param point_id: 核心点
    :param eps: 同一域下样本最大距离
    :return:
    """
    n_points = data.shape[0]
    seeds = []
    for i in range(0, n_points):
        if __eps_neighborhood(data[point_id, :], data[i, :], eps):
            seeds.append(i)
    return seeds


def __expand_cluster(data, classifications, point_id, cluster_id, eps, min_points):
    """
    类簇扩散
    :param data: 数据集,array
    :param classifications: 分类结果
    :param point_id: 当前点
    :param cluster_id: 分类类别
    :param eps: 同一域下样本最大距离
    :param min_points: 每个簇最小核心点数
    :return:
    """
    seeds = __region_query(data, point_id, eps)
    if len(seeds) < min_points:
        classifications[point_id] = NOISE
        mark = False
    else:
        classifications[point_id] = cluster_id
        for seed_id in seeds:
            classifications[seed_id] = cluster_id
        while len(seeds) > 0:
            current_point = seeds[0]
            results = __region_query(data, current_point, eps)
            if len(results) >= min_points:
                for i in range(0, len(results)):
                    result_point = results[i]
                    if classifications[result_point] == UNCLASSIFIED or classifications[result_point] == NOISE:
                        if classifications[result_point] == UNCLASSIFIED:
                            seeds.append(result_point)
                        classifications[result_point] = cluster_id
            seeds = seeds[1:]
        mark = True
    return mark


def dbscan(data, eps, min_points):
    """
    dbscan聚类
    :param data: 数据集,array
    :param eps: 同一域下样本最大距离
    :param min_points: 每个簇最小核心点数
    :return:
    """
    cluster_id = 1
    n_points = data.shape[0]
    classifications = [UNCLASSIFIED] * n_points
    for point_id in range(0, n_points):
        if classifications[point_id] == UNCLASSIFIED:
            if __expand_cluster(data, classifications, point_id, cluster_id, eps, min_points):
                cluster_id = cluster_id + 1
    return classifications


if __name__ == "__main__":
    img_file = r'H.png'
    max_score = -1000
    renders = []
    best_k = -1
    raw_img = Image.open(img_file)
    img = cv2.imread(img_file)
    data = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    data = data.reshape((-1, 3))
    dbscan = dbscan(data, 0.1, 3)

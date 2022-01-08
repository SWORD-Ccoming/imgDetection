import time

import requests # 导入requests库
import os # 导入os模块
from requests.adapters import HTTPAdapter
from requests import Response


def down_pic(url, filename):
    '''定义一个函数，用于下载网络图片，参数url为图片对应的url地址，filename为爬取图片名字'''
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    r = s.get(url, timeout=(10, 10))
    # requests.get(url, timeout=(10, 10))
     # 获取网页内容
    path = 'C:/Users/ROG/Desktop/test' # 爬取图片待存储目录
    if not os.path.exists(path): # 判断桌面是否有一个名称为“图片”的文件夹，如果没有，就创建它
        os.mkdir(path)    # 爬取图片
    with open(path + '\\' + filename, 'wb') as f:
        f.write(r.content) # 以二进制形式写入文件
        f.close # 关闭文件

if __name__ == '__main__':
    imagesNumber = ['21', '18', '15', '12', '09', '06', '03', '00']
    for i in range(8):
        # for j in range(3):
        #     if j == 0:
        url = 'http://www.nmc.cn/product/2021/12/16/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_2021121' + str(6) + imagesNumber[i] + '0000000.jpg'
        down_pic(url, str(i) + '.jpg')
        print('成功执行' + str(i) + '次')

    # url = 'http://www.nmc.cn/product/2021/12/18/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_20211218000000000.jpg' # 图片对应的url地址
    # time.sleep(5)
    # down_pic(url, 'dog.jpg') # 调用函数

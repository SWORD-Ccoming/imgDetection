from PIL import Image
import os
import numpy as np
input_dir = 'E:/102/'
out_dir = 'E:/103/'
a = os.listdir(input_dir)

for i in a:
    print(i)
    L = Image.open(input_dir + i)
    # L = I.convert('1')
    matrix = 255 - np.asarray(L)  # 图像转矩阵 并反色
    for j in range(0, matrix.shape[0]):
        for k in range(0, matrix.shape[1]):
            if(matrix[j][k] != 255):
                matrix[j][k] = 0
    new_img = Image.fromarray(matrix)  # 矩阵转图像
    new_img.save(out_dir + i)  # 保存图片

    # L.save(out_dir + i)

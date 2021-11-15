import cv2
import numpy as np


def img_resize_to_target_black(image):
	target = np.zeros((500, 500), dtype=np.uint8)
	bgr_img = cv2.cvtColor(target, cv2.COLOR_GRAY2BGR)
	h = image.shape[0]
	w = image.shape[1]
	position = 230
	for i in range(h):
		for j in range(w):
			bgr_img[i+position, j+position, 0] = image[i, j, 0]
			bgr_img[i+position, j+position, 1] = image[i, j, 1]
			bgr_img[i+position, j+position, 2] = image[i, j, 2]
	return bgr_img


if __name__ == '__main__':
	image = cv2.imread('1.png')
	img_new_black = img_resize_to_target_black(image)
	cv2.imshow("img_new_black", img_new_black)
	cv2.imwrite("1black.png", img_new_black)
	cv2.waitKey()
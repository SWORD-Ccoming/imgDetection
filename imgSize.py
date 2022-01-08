import cv2
for i in range(20):
    img = cv2.imread('C:/Users/ROG/Desktop/testset/' + str(0 + i + 1) + '.jpg')
    print(img.shape)
    cv2.imwrite('C:/Users/ROG/Desktop/result3/P000' + str(200 + i + 1) + '__1__0___0' + '.png', img)
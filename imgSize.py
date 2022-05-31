import cv2
count = 0
for i in range(195):

    img = cv2.imread('C:/Users/ROG/Documents/Tencent Files/1004747472/FileRecv/detection(1)_195/P000200' + str(i) + '__1__0___0.png')
    # if(img.shape[0] == 860):
    #     cv2.imwrite('C:/Users/ROG/Desktop/data/test3/1(' + str(i + 1) + ').png', img)
    #     count += 1
    #     print(count)
    print(img.shape);
    # cv2.imwrite('C:/Users/ROG/Desktop/result3/P000' + str(200 + i + 1) + '__1__0___0' + '.png', img)

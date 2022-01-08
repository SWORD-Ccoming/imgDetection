import cv2

data = cv2.imread("louchaoqiang.jpg");
data = cv2.cvtColor(data, cv2.COLOR_BGR2HSV);
H, S, V = cv2.split(data);
print(H, S, V)
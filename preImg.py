import cv2
from PIL import Image,ImageDraw
import math
def rotatePoint(xc, yc, xp, yp, theta):
    xoff = xp - xc;
    yoff = yp - yc;
    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    pResx = cosTheta * xoff + sinTheta * yoff
    pResy = - sinTheta * xoff + cosTheta * yoff
    return str(int(xc + pResx)), str(int(yc + pResy))
image_path = 'C:/Users/ROG/Desktop/mydataset/images/P0001__1__0___0.png'
image = Image.open(image_path)
# cx = 836.0518
# cy = 543.2503
# w = 90.1011
# h = 26.6469
# angle = 0

# x0, y0 = rotatePoint(cx, cy, cx - w / 2, cy - h / 2, -angle)
# x1, y1 = rotatePoint(cx, cy, cx + w / 2, cy - h / 2, -angle)
# x2, y2 = rotatePoint(cx, cy, cx + w / 2, cy + h / 2, -angle)
# x3, y3 = rotatePoint(cx, cy, cx - w / 2, cy + h / 2, -angle)
# angle = math.degrees(angle)
x0 = int(804)
x1 = int(770)
x2 = int(771)
x3 = int(805)
y0 = int(762)
y1 = int(762)
y2 = int(739)
y3 = int(739)



# 创建一个可以在给定图像上绘图的对象
# draw = ImageDraw.Draw(image)
# draw.polygon([(2361,700), (2276,699), (2276,683), (2361,681)], outline=(255,0,0))
# image.show()

draw = ImageDraw.Draw(image)
draw.polygon([(x0, y0), (x1, y1), (x2, y2), (x3, y3)], outline=(255,0,0))
image.show()
# print(angle)
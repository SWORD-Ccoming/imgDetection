from matplotlib import pyplot as plt
plt.xlabel("簇的数量",fontproperties="STSong")
plt.ylabel("误差平方和",fontproperties="STSong")
# plt.title("簇的选取手肘法展示图",fontproperties="STSong")
x=range(1,9,1)
y=[1700,1300,700,400,350,300,270,200]
#绘图
plt.plot(x,y)
#展示
plt.show()
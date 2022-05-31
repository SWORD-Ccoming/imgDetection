import os

path = r"E:\实验一数据集\photo1"
files = os.listdir(path)
i = 0

for sub_dir in files:
	newName = 'P000' + str(i) + '__1__0___0.xml'
	os.rename(path + "\\" + sub_dir, path+"\\"+newName)
	i = i + 1
def read_json_save_to_txt():
	import json
	import os
	from glob import glob

	dir_json = r"E:/91/"  # json文件的目录

	jsons = glob(dir_json + "*.json", recursive=False)  # 搜寻该目录下所有后缀名为.json的文件路径，改为**/*.json recursive=True为所有子目录的
	all_files = glob(dir_json + "*.*", recursive=False)

	images = list(set(all_files).difference(set(jsons)))  # all_files中有而jsons中没有的,就是图片
	# with open(dir_json + 'points_data' + '.txt', "w") as txt:
	for file in jsons:
		textNameList = str(file).split('.')
		with open(str(textNameList[0]) + '.txt', "w") as txt:
			with open(file, 'r') as load_f:
				load_dict = json.load(load_f)
				# print("load_dict:", load_dict)
				for index in range(len(load_dict["shapes"])):
					label = load_dict["shapes"][index]["label"]  # 读取json中的标签信息
					points = load_dict["shapes"][index]["points"]  # 读取json中的点的信息
					points = [int(j) for i in points for j in i]  # 所有的点化为整数

					# for i in images:
						# textNameList = str(i).split('.')
						# with open(str(textNameList[0]) + '.txt', "w") as txt:
						# if file.split(".")[0] == i.split(".")[0]:
					txt.writelines("{0},{1}\n".format(",".join(str(i) for i in points), label))

read_json_save_to_txt()


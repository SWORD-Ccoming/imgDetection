import time

import pyautogui
import datetime
import threading
nowTime = datetime.datetime.now()
time1_str = datetime.datetime.strftime(nowTime, '%Y-%m-%d %H:%M:%S')
time1_str = time1_str.split()

print(nowTime, time1_str)


def func():
	screenWidth, screenHeight = pyautogui.size() # 屏幕尺寸
	mouseX, mouseY = pyautogui.position()
	# pyautogui.moveTo(screenWidth/2, screenHeight/2) # 基本移动
	# pyautogui.moveTo(screenWidth/2, screenHeight/2, duration=2) # 移动过程持续2s完成
	# pyautogui.moveTo(None, 500) # X方向不变，Y方向移动到500
	pyautogui.click(button='left')
	# pyautogui.moveRel(-40, 500) # 相对位置移动


now_time = datetime.datetime.now()
time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
strList = time1_str.split()
numberList = strList[1].split(':')
# for i in range(100):
# 	if int(numberList[2]) >= 50:
# 		next_time = datetime.datetime.strptime(
# 		str(strList[0]) + ' ' + str(numberList[0]) + ':' + str(int(numberList[1]) + 1) + ':' + str((int(numberList[2]) + 10) - 60), "%Y-%m-%d %H:%M:%S")
#
# 		timer_start_time = (next_time - now_time).total_seconds()
# 		print(timer_start_time)
# 		# 54186.75975
#
# 		# 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
# 		timer = threading.Timer(timer_start_time, func)
# 		timer.start()
# 		time.sleep(9)
# 	else:
# 		next_time = datetime.datetime.strptime(
# 		str(strList[0]) + ' ' + str(numberList[0]) + ':' + str(numberList[1]) + ':' + str(int(numberList[2]) + 10), "%Y-%m-%d %H:%M:%S")
#
# 		timer_start_time = (next_time - now_time).total_seconds()
# 		print(timer_start_time)
# 		# 54186.75975
#
# 		# 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
# 		timer = threading.Timer(timer_start_time, func)
# 		timer.start()
# 		time.sleep(9)
next_time = datetime.datetime.strptime(str(strList[0]) + ' ' + str(numberList[0]) + ':' + str(numberList[1]) + ':' + str(20), "%Y-%m-%d %H:%M:%S")

timer_start_time = (next_time - now_time).total_seconds()
print(timer_start_time)
# # 54186.75975
#
#
# 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
timer = threading.Timer(timer_start_time, func)
timer.start()

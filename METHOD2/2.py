# STATUS: fail and directly go to 3.py
import numpy as np
import cv2
import statistics

image_path = '.\\1.jpg'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)

BK_Color = np.zeros((len(img),1, 3))
# print(state.shape)
# print(img, "getpixel value")
i = 100
total_time = 1
time_rate = 1
state = np.zeros((len(img),total_time, 3, time_rate))
state = img[100:200, 304,:]
print(BK_Color)
state[i, 304, :, 1]
BK_Color[i, 0, :]
mean = state[i, 304, :, 1]-BK_Color[i, 304, :]
print(mean)
# """
# for timing in range(0, MAX):
#     a[:,timing] = img[:,304,:] # time_color[]
#     # img = [1, 2, 3, ... MAX_x][1, 2, 3, ... MAX_x][R G B]
#     # HENCE, img[:,304,:] == [1, 2, 3, ... MAX_x][304][R G B]
#     # a = [1, 2, 3, ... MAX_x][time1, time2, ...]
# BK_Color = max(a,key=a.count)
# """
# """
# # 获取list中出现次数最多的元素
# a = [1,2,3,4,2,3,2]
# maxlabel = max(a,key=a.count)
# print(maxlabel)
# """
# print(state.shape,"state.shape")

# for i in range(100,200):
#     # i = 100

#     # new car comes by!
#     # detect every 1 sec (aka 30 frames)
# # if T%30 == 0:
# # state[i, 304, :]
#     state = img[i,304,:]
#     img[304,304,:]
#     print(state, "getpixel value")

#     # for i in range(0, ):

#     # compare(state, BK_Color)

#     # meanU = statistics.mean(state[i, 304, :]-BK_Color[i, 304, :])
#     # meanD = statistics.mean(BK_Color[i, 304, :])
#     # mean = meanU/meanD

#     print(state.shape)
#     # mean = state[i, 304, :]-BK_Color[i, 304, :]
#     if  mean > 0.8:
#         # return state[i, 304, :]
#         print("found car")
#         carNum += 1


# print(img.shape)
# cv2.imshow('image',img)
# cv2.waitKey(0)

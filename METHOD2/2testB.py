import numpy as np
import cv2
import statistics

image_path = '.\\1.jpg'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)

state = np.zeros(len(img))
# print(img, "getpixel value")

BK_Color = img[100:200,304,:]
print(BK_Color)
"""
for timing in range(0, MAX):
    a[:,timing] = img[:,304,:] # time_color[]
    # img = [1, 2, 3, ... MAX_x][1, 2, 3, ... MAX_x][R G B]
    # HENCE, img[:,304,:] == [1, 2, 3, ... MAX_x][304][R G B]
    # a = [1, 2, 3, ... MAX_x][time1, time2, ...]
BK_Color = max(a,key=a.count)
"""
"""
# 获取list中出现次数最多的元素
a = [1,2,3,4,2,3,2]
maxlabel = max(a,key=a.count)
print(maxlabel)
"""

# for i in range(100,200):
    # new car comes by!
    # detect every 1 sec (aka 30 frames)
# if T%30 == 0:
# state[i, 304, :]
i = 100
state = img[i,304,:]
img[304,304,:]
print(state, "getpixel value")

print(state[i, 304, :])

# compare(state, BK_Color)
mean = state[i, 304, :]-BK_Color[i, 304, :]
if  mean > 0.8:
    # return state[i, 304, :]
    print("found car")
    carNum += 1


print(img.shape)
cv2.imshow('image',img)
cv2.waitKey(0)

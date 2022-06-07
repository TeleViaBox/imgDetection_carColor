# STATUS: SUCCESS
# AUTHOR: ALEXLEE

import numpy as np
import cv2
image_path = '.\\1.jpg'
# import cv2.cv
# img = cv2.imread('./images/1.jpg')
# img = cv2.imread(image_path)

# img = cv2.imread('./1.jpg')
# img = cv2.cv.LoadImage(image_path, CV_LOAD_IMAGE_COLOR)
# img = cv2.cv.LoadImage(image_path, cv2.IMREAD_COLOR)

# img = cv2.cv.LoadImage("./1.jpg", CV_LOAD_IMAGE_COLOR)
# img = cv2.imread(image_path, cv2.CV_LOAD_IMAGE_COLOR)

# 将cv2.CV_LOAD_IMAGE_COLOR改为cv2.IMREAD_COLOR
img = cv2.imread(image_path, cv2.IMREAD_COLOR)


print(img, "getpixel value")
print(img[304,304,:], "getpixel value")
# print(img)

px = img[88, 99]
print(px) #[32, 31, 47]
# 只取得藍色
blue = img[88, 99, 0]  # []中的第0項
print(blue) # 32

# print(len(img))
print(img.shape)
# for i in range(1, 1000):
#     img[100, 100, 2] = [255, 255, 255]
# print(img[88, 99]) #[255, 255, 255]

cv2.imshow('image',img)
cv2.waitKey(0)

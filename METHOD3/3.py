import numpy as np
import statistics
import cv2
import glob
import os

# 變更到指定尺寸，長寬邊不足者補黑色
def process_image(img, min_side = 608):
    size = img.shape
    h, w = size[0], size[1]
    scale = max(w, h) / float(min_side)
    new_w, new_h = int(w/scale), int(h/scale)
    resize_img = cv2.resize(img, (new_w, new_h),cv2.INTER_AREA) # 變更尺寸
    if new_w % 2 != 0 and new_h % 2 == 0:
        top, bottom, left, right = (min_side-new_h)//2, (min_side-new_h)//2, (min_side-new_w)//2 + 1, (min_side-new_w)//2
    elif new_h % 2 != 0 and new_w % 2 == 0:
        top, bottom, left, right = (min_side-new_h)//2 + 1, (min_side-new_h)//2, (min_side-new_w)//2, (min_side-new_w)//2
    elif new_h % 2 == 0 and new_w % 2 == 0:
        top, bottom, left, right = (min_side-new_h)//2, (min_side-new_h)//2, (min_side-new_w)//2, (min_side-new_w)//2
    else:
        top, bottom, left, right = (min_side-new_h)//2 + 1, (min_side-new_h)//2, (min_side-new_w)//2 + 1, (min_side-new_w)//2
    pad_img = cv2.copyMakeBorder(resize_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0]) 
    return pad_img

# 讀寫目錄
inputPath = './'
outputPath = './images'

files = os.path.join(inputPath,'*.mp4')
files_grabbed = []
files_grabbed.extend(sorted(glob.iglob(files)))

for videoId in range(len(files_grabbed)):
	print(files_grabbed[videoId])
	raw = cv2.VideoCapture(files_grabbed[videoId])
	fIndex = 1
	fCount = 0

	while 1:
    # 影片轉圖片
	    ret,frame = raw.read()
	    fCount += 1
	    if (ret == True) :
	    	if (fCount % 5) == 0:
                img_pad = process_image(frame, min_side = 608)
                cv2.imshow('image',img)
                cv2.waitKey(0)
                cv2.imwrite('%s/%02d-frame-608x608-%04d.jpg' % (outputPath, videoId,fIndex), img_pad)
                fIndex += 1
	    else:
	    	break




# image_path = '.\\1.jpg'
# image_path = '%s/%02d-frame-608x608-%04d.jpg'  (, videoId,fIndex), img_pad
# img = cv2.imread(image_path, cv2.IMREAD_COLOR)
# # BK_Color = np.zeros((len(img),1, 3))
# i = 100
# total_time = 1
# time_rate = 1
# # state = np.zeros((len(img),total_time, 3, time_rate))
# state = img[100:200, 304,:]
# print(state.shape)
# meanUp = 0
# meanDown = 0
# BK_Color = 100*state
# countCar = 0
# for f in range(0,99):
#     # meanUp += state[f,:] - BK_Color[f,:]
#     meanUp += state[f,:]
#     meanDown += BK_Color[f,:]
# print(meanUp, meanDown)
# # meanUp.dtype = 'int'
# # print(int(meanUp[]), int(meanDown))
# # print(meanUp[0])
# while 1:
#     # for frame in range(1):
    
#     image_path = './' + str(frame) + '.jpg'
#     img = cv2.imread(image_path, cv2.IMREAD_COLOR)
#     colorCar = np.zeros(100)
#     meanUpTotal = meanUp[0] + meanUp[1] + meanUp[2]
#     meanDownTotal = meanDown[0] + meanDown[1] + meanDown[2]
#     if (meanUpTotal-meanDownTotal)/(meanDownTotal) > 0.8:
#         print("Find new car!")
#         countCar += 1
#         colorCar[countCar-1] = meanUp
#         print(colorCar, "heoo")

    
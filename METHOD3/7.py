import cv2
import glob
import os
import numpy as np
# # 變更到指定尺寸，長寬邊不足者補黑色
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

if os.path.isdir('images') != True:
    os.mkdir('.\\images')    
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
                    cv2.imwrite('%s/%d-frame-608x608-%d.jpg' % (outputPath, videoId,fIndex), img_pad)
                    fIndex += 1
            else:
                break

# Background = np.zeros(674)
Background = [0] * 674
Background_sum = [0] * 674
for num in range(1, 674):
    image_path = './images/0-frame-608x608-'+ str(num) +'.jpg'
    # image_path = '%s/%02d-frame-608x608-%04d.jpg'  (, videoId,fIndex), img_pad
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    state = img[100:200, 304,:]
    meanUp = np.zeros(800)
    meanDown = 0
    BK_Color = 100*state
    countCar = 0
    # print(state[num, 1])
    print(state.shape)

    # for rgb in range(0,2):
    for x_axis in range(0,99):
        BK_Color[x_axis, 0] = state[x_axis, 0] + state[x_axis, 1] + state[x_axis, 2]
        # BK_Color[x_axis, 1] = state[x_axis, 0] + state[x_axis, 1] + state[x_axis, 2]
        # BK_Color[x_axis, 2] = state[x_axis, 0] + state[x_axis, 1] + state[x_axis, 2]

        # print(BK_Color[x_axis, 0])
        Background_sum[num] += Background[num]
        
    Background[num] += BK_Color[:,0]
    print(Background[num], "num")
    print((Background_sum[num]), "sum")
    # cv2.waitKey(0)
    # Background_sum[num] += Background[num]
    # print(Background_sum)
    # cv2.waitKey(0)


for num in range(1, 674):
    image_path = './images/0-frame-608x608-'+ str(num) +'.jpg'
    # image_path = '%s/%02d-frame-608x608-%04d.jpg'  (, videoId,fIndex), img_pad
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    state = img[100:200, 304,:]
    meanUp = np.zeros(800)
    meanDown = 0
    BK_Color = 100*state
    countCar = 0
    # print(state[num, 1])
    # print("final")
    # print(Background[num]) # RESULT:RUNNABLE, clear
    # print(Background) # RESULT:RUNNABLE, dirty
    for x_axis in range(0,99):
        BK_Color[x_axis, 0] = state[x_axis, 0] + state[x_axis, 1] + state[x_axis, 2]
    # print(BK_Color[:,0], "BK!")
    # print(Background[num], "Backround!")
    
    # print(BK_Color[:,0] - Background[num], "MAN!")
    
    ########
    # 7.py:88: RuntimeWarning: overflow encountered in ubyte_scalars
    # BK_Color[x_axis, 0] = state[x_axis, 0] + state[x_axis, 1] + state[x_axis, 2]
    # Traceback (most recent call last):
    # File "7.py", line 89, in <module>
    # print(BK_Color[:,0] - Background, "YO!")
    # ValueError: operands could not be broadcast together with shapes (100,) (674,)
    ########

    # print(len(Background), "len") # RESULT: 674 len
    # print(BK_Color.shape, "BK_Color")
    # print(Background, "BACKGROUND")
    # Background[num] = BK_Color[:,0]
        # THIS HAS NO WARNNING! why? print(BK_Color[x_axis])
        # print(BK_Color[x_axis, 0]) vs print(BK_Color[x_axis])
        # meanUp[num] = int(state[:, 0]) 
        # + int(state[num, 1]) + int(state[num, 2])

    # print(meanUp[num], "hello")
    # # for f in range(0,99):
    # #     # meanUp += state[f,:] - BK_Color[f,:]
    # #     meanUp[num, ] += state[f,:]
    # #     meanDown += BK_Color[f,:]
    # print(meanUp, meanDown)
    # meanUpTotal = meanUp[0] + meanUp[1] + meanUp[2]
    # meanDownTotal = meanDown[0] + meanDown[1] + meanDown[2]
    # if (meanUpTotal-meanDownTotal)/(meanDownTotal) > 0.8:
    #     print("Find new car!")
    #     # countCar += 1
    #     # colorCar[countCar-1] = meanUp
    #     # print(colorCar, "heoo")


# # BK_Color = np.zeros((len(img),1, 3))
# i = 100
# total_time = 1
# time_rate = 1
# # state = np.zeros((len(img),total_time, 3, time_rate))

# print(state.shape)

# # meanUp.dtype = 'int'
# # print(int(meanUp[]), int(meanDown))
# # print(meanUp[0])
# while 1:
#     # for frame in range(1):
    
#     image_path = './' + str(frame) + '.jpg'
#     img = cv2.imread(image_path, cv2.IMREAD_COLOR)
#     colorCar = np.zeros(100)

    


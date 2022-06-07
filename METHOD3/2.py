# from METOHD2_the5
import cv2
import glob
import os
import numpy as np
import statistics

files = os.path.join(inputPath,'*.mp4')
files_grabbed = []
files_grabbed.extend(sorted(glob.iglob(files)))

for videoId in range(len(files_grabbed)):
	print(files_grabbed[videoId])
	raw = cv2.VideoCapture(files_grabbed[videoId])
	fIndex = 1
	fCount = 0

	while 1:
    # video to img
	    ret,frame = raw.read()
	    fCount += 1
	    if (ret == True) :
	    	if (fCount % 500) == 0:
		    	img_pad = process_image(frame, min_side = 608)                
                image_path = '.\\1.jpg'
                img = cv2.imread(image_path, cv2.IMREAD_COLOR)
                # BK_Color = np.zeros((len(img),1, 3))
                i = 100
                total_time = 1
                time_rate = 1
                # state = np.zeros((len(img),total_time, 3, time_rate))
                state = img[100:200, 304,:]
                print(state.shape)
                meanUp = 0
                meanDown = 0
                BK_Color = 100*state
                countCar = 0
                for f in range(0,99):
                    # meanUp += state[f,:] - BK_Color[f,:]
                    meanUp += state[f,:]
                    meanDown += BK_Color[f,:]
                print(meanUp, meanDown)
                # meanUp.dtype = 'int'
                # print(int(meanUp[]), int(meanDown))
                # print(meanUp[0])
                while 1:
                    # for frame in range(1):
                    
                    image_path = './' + str(frame) + '.jpg'
                    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
                    colorCar = np.zeros(100)
                    meanUpTotal = meanUp[0] + meanUp[1] + meanUp[2]
                    meanDownTotal = meanDown[0] + meanDown[1] + meanDown[2]
                    if (meanUpTotal-meanDownTotal)/(meanDownTotal) > 0.8:
                        print("Find new car!")
                        countCar += 1
                        colorCar[countCar-1] = meanUp
                        print(colorCar, "heoo")
		    	# cv2.imwrite('%s/%02d-frame-608x608-%04d.jpg' % (outputPath, videoId,fIndex), img_pad)
		    	fIndex += 1
	    else:
	    	break
    
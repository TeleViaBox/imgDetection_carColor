
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
		    	cv2.imwrite('%s/%02d-frame-608x608-%04d.jpg' % (outputPath, videoId,fIndex), img_pad)
		    	fIndex += 1
	    else:
	    	break

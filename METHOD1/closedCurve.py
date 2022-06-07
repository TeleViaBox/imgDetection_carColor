# AUTHOR: totally OTHER's
# REF: https://blog.csdn.net/qq_25254777/article/details/80238444

import numpy as np
import cv2

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,start_x,start_y

    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing == False:
            start_x, start_y = x,y
            ix,iy = x,y
            drawing = True
        elif drawing == True:
            cv2.line(img,(ix,iy),(x,y),(0,255,0),3)
            ix, iy = x, y
        print(drawing)
    elif event == cv2.EVENT_MBUTTONDOWN:
        drawing = False

        cv2.line(img, (ix, iy), (start_x, start_y), (0, 255, 0), 3)
        print(drawing)


    #
    # elif event == cv2.EVENT_RBUTTONUP:
    #     cv2.line(img,(ix,iy),(x,y),(0,255,0),3)
# Next we have to bind this mouse callback function to OpenCV # # window. In the main loop, we should set a keyboard binding for
# key ‘m’ to toggle between rectangle and circle.
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'): # 切换模式
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
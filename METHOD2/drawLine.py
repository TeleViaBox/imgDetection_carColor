import cv2
# capture=cv2.VideoCapture(0)
img=cv2.imread('./images/00-frame-608x608-0003.jpg',1)
cv2.line(img,(0,0),(1000,1000),color=(255,255,255),thickness=5)
# 从（0，0）-》（100，100）颜色（BGR 255 是蓝）宽度是5
cv2.imshow('image',img)
cv2.waitKey(0)
# while (True):
#     ref, frame = capture.read()
#     cv2.line(frame,(0,0),(100,100),color=(255,0,0),thickness=5)
#     cv2.imshow("video", frame)
# 
#     c = cv2.waitKey(1) & 0xff
#     if c == 27:
#         capture.release()
#         break

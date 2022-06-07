import cv2
img=cv2.imread('./images/00-frame-608x608-0003.jpg',1)

size = img.shape
startPoint = (0, int(size[1]/2))
endPoint = (int(size[0]), int(size[1]/2))
print(startPoint)
print(endPoint)

# get the array of the middle-horizontal line

cv2.line(img,startPoint,endPoint,color=(255,255,255),thickness=5)
cv2.imshow('image',img)
cv2.waitKey(0)
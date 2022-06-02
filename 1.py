# step1 find the cars
# step2 again, use the color to count

# to detect where and which object is the car,
# I can detect the "traffic lane line", 
# and the object between the lines have high possibility 
# of being as a car

# Complextiy Ana.

# Erosion Algorithm

# step2 to discriminate which is the background.

# ISSUE: one object could have multiple colors
# sol: the biggest portion of color is mostly often the color of the car

# MEASURMENT: how to debug and how to check the quality of the program.

# OTHER's method
# 1. noise reducing 2. contours, and then draw the contours
# 3. find closed curves, and then remove the unclosed curves
# 4. 


import cv2

def fdf:
    sf
def     

frame = input(VIDEO)

ret, output = cv2.THRESH_BINARY(img, thresh, maxval, type)

########################################################################################
# ref: https://onway2017.wordpress.com/2021/04/21/python-%E5%BD%B1%E5%83%8F%E8%99%95%E7%90%86-opencv-%EF%BC%8815%EF%BC%89%EF%BC%9A%E5%BD%B1%E5%83%8F%E8%BC%AA%E5%BB%93/
# findContours
import cv2 as cv
img = cv.imread("black.png")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪
ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# 尋找輪廓
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(len(contours[0]))
########################################################################################
import cv2 as cv
 
img = cv.imread("black.png")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("img", img)
# 降噪
ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# 尋找輪廓
contours, hierarchy = cv.findContours(gray_img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(len(contours[0]))
# 繪製綠色輪廓
cv.drawContours(img, contours, -1, (0,255,0), 3)
cv.imshow("draw", img)
cv.waitKey(0)
cv.destroyAllWindows()
########################################################################################



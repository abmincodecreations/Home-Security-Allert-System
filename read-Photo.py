import cv2 as cv
# reading images
img = cv.imread('Photos/c-1.jpg')
# code to show matrix image variable img
cv.imshow('Cat', img)

cv.waitKey(0)
import cv2 as cv
# reading images


def rescaleFrame( frame , scale=0.15):
  #FRAME.SHAOE-O IS WIDTH AND FRAME.SHAPE-1 IS HEIGHT AND VALUE RETURNED ISA FLOATING VALUE WHICH WE HAVE TO CONVERT IT INTO INTIGER USING int()
  width=int(frame.shape[1]*scale)
  height=int(frame.shape[0]*scale)
  dimensions=(width, height)

  return cv.resize(frame , dimensions, interpolation=cv.INTER_AREA)
#videocapture captures 0 , 1 and so on camera ports attached and it also accepts path address

img = cv.imread('Photos/c-1.jpg')
# code to show matrix image variable img
resize_image =rescaleFrame(img)
cv.imshow('Cat', resize_image)

capture= cv.VideoCapture('videos/p-vid.mp4')

while True:
  #here we store videos i the form of indivisual frames 
  isTrue , frame = capture.read()
  #reads video captured frame by frame

  frame_resized = rescaleFrame(frame)
  cv.imshow('video' , frame)
  cv.imshow('video_resized' , frame_resized)
  #cv2.error: OpenCV(4.6.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:967: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow' this error is shown when path is incorrrect or frames is over here ord is passed with d as a input 

  if cv.waitKey(1) & 0xFF == ord('d'):
    break
capture.release()



cv.destroyWindow()

cv.waitKey(0)

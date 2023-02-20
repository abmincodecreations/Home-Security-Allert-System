import cv2 as cv

#videocapture captures 0 , 1 and so on camera ports attached and it also accepts path address
capture= cv.VideoCapture('videos/p-vid.mp4')

while True:
  #here we store videos i the form of indivisual frames 
  isTrue , frame = capture.read()
  #reads video captured frame by frame
  cv.imshow('video' , frame)
  #cv2.error: OpenCV(4.6.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:967: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow' this error is shown when path is incorrrect or frames is over here ord is passed with d as a input 

  if cv.waitKey(1) & 0xFF == ord('d'):
    break
capture.release()
cv.destroyWindow()

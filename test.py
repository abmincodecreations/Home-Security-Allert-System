from gtts import gTTS
import os
import cv2
import cv2 as cv
import numpy
import face_recognition

def faceRecognition(image1 , image2):

  img = cv2.imread(image1)
  rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  img_encoding = face_recognition.face_encodings(rgb_img)[0]


  img2 = cv2.imread(image2)
  rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
  img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]


  result = face_recognition.compare_faces([img_encoding], img_encoding2)
  print("Result: ", result)
  return result

def faceDetector(capturingData ):
                # load the required trained XML classifiers
                # https://github.com/Itseez/opencv/blob/master/
                # data/haarcascades/haarcascade_frontalface_default.xml
                # Trained XML classifiers describes some features of some
                # object we want to detect a cascade function is trained
                # from a lot of positive(faces) and negative(non-faces)
                # images.
                face_cascade = cv2.CascadeClassifier('HarCascadeFrontalFace.xml')
                
                # https://github.com/Itseez/opencv/blob/master
                # /data/haarcascades/haarcascade_eye.xml
                # Trained XML file for detecting eyes
                eye_cascade = cv2.CascadeClassifier('HarCascadeEye.xml') 
                
                # capture frames from a camera
                cap = capturingData
                
                # loop runs if capturing has been initialized.
                while 1: 
                
                    # reads frames from a camera
                    ret, img = cap.read() 
                    
                    # convert to gray scale of each frames
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                    # Detects faces of different sizes in the input image
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    
                    for (x,y,w,h) in faces:
                        # To draw a rectangle in a face 
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
                        roi_gray = gray[y:y+h, x:x+w]
                        roi_color = img[y:y+h, x:x+w]
                        personDetected = True
                        print(personDetected)
                        # Detects eyes of different sizes in the input image
                        eyes = eye_cascade.detectMultiScale(roi_gray) 
                
                        #To draw a rectangle in eyes
                        for (ex,ey,ew,eh) in eyes:
                            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
                        
                
                    # Display an image in a window
                    output=cv2.imshow('img',img)

                

               
                return output

def CameraOnFaceDetection():
          key = cv2. waitKey(1)
          webcam = cv2.VideoCapture(0)
          while True:
              try:
                  check, frame = webcam.read()
                  # print(check) #prints true as long as the webcam is running
                  #print(frame) #prints matrix values of each framecd 
                  faceDetector(webcam)
                  key = cv2.waitKey(1)
                  if key == ord('s'): 
                      cv2.imwrite(filename='saved_img.jpg', img=frame)
                      webcam.release()
                      img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                      # img_new = cv2.imshow("Captured Image", img_new)
                      cv2.waitKey(1650)
                      cv2.destroyAllWindows()
                      print("Processing image...")
                      img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                      print("Converting RGB image to grayscale...")
                      gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                      print("Converted RGB image to grayscale...")
                      print("Resizing image to 28x28 scale...")
                      img_ = cv2.resize(gray,(28,28))
                      print("Resized...")
                      img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                      print("Image saved!")
                      faceDetector(webcam)
                      break
                  elif key == ord('q'):
                      print("Turning off camera.")
                      webcam.release()
                      print("Camera off.")
                      print("Program ended.")
                      cv2.destroyAllWindows()
                      break
              except(KeyboardInterrupt):
                  print("Turning off camera.")
                  webcam.release()
                  print("Camera off.")
                  print("Program ended.")
                  cv2.destroyAllWindows()
                  break


CameraOnFaceDetection()


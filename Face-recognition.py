from cv2 import (VideoCapture, namedWindow, imshow, waitKey, destroyWindow, imwrite)
from gtts import gTTS
import os
import cv2
import cv2 as cv
import numpy
import face_recognition

language='en'

cam_port = 0
cam = VideoCapture(cam_port)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error,
# show result
if result:
	  imwrite("images/Geeks.jpg", image)
else:
	  print("No image detected. Please! try again #")

Image1="images/Geeks.jpg"
Image2="images/My-Face.jpg"

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


UnkownText="Unknown Person Detected Pakdo re Pakdo chor aya"
myText= "Abhishek is at the door"

def speaker(text):
  output=gTTS(text=myText,lang=language,slow=False)
  output.save("output.mp3")
  os.system("start output.mp3")
  print('playing sound using  playsound')



if "[True]"==str(faceRecognition(Image1 , Image2)):
   speaker(myText)
else:
  speaker(UnkownText)



  
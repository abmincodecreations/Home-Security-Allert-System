from cv2 import (VideoCapture, namedWindow, imshow, waitKey, destroyWindow, imwrite)
from playsound import playsound
from gtts import gTTS
import os
import cv2
import cv2 as cv
import numpy
import face_recognition
import time
import pywhatkit
import keyboard as k
import serial

language='en'
UnkownText="Someone is at the door let me check who's it, it's a Unknown new person  "
myText= "Someone is at the door let me check who's it , it's Abhishek  at the door"
Image1="images/Geeks.jpg"
Image2="images/My-Face.jpg"
Face_Detected = False
Similarface=False


def speaker(textt):
    output=gTTS(text=textt,lang=language,slow=False)
    output.save("output.mp3")
    #os.system("start output.mp3")
    playsound('output.mp3')
    print('playing sound using  playsound')
    os.remove('output.mp3')

def sendWhatsAppMsg(text):
   img='images/Geeks.jpg'
   pywhatkit.sendwhats_image('+917894653860',img,text,15,False,3)
   k.press_and_release('enter')


def faceRecognition(image1 , image2 ):

  img = cv2.imread(image1)
  rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  img_encoding = face_recognition.face_encodings(rgb_img)[0]


  img2 = cv2.imread(image2)
  rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
  img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]


  result = face_recognition.compare_faces([img_encoding], img_encoding2)
  print("Result: ", result)
  global Similarface
  Similarface=False
  Similarface=result
  return result
  
def faceDetector():
                global Similarface
                face_cascade = cv2.CascadeClassifier('HarCascadeFrontalFace.xml')
            
                eye_cascade = cv2.CascadeClassifier('HarCascadeEye.xml') 
                
                # capture frames from a camera image.png

                
                cap = cv2.VideoCapture(0)
                check, frame = cap.read()
                # loop runs if capturing has been initialized.
                while 1: 
                
                    # reads frames from a camera
                    ret, img = cap.read() 
                    
                    # convert to gray scale of each frames
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                    # Detects faces of different sizes in the input image
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    if str(faces) == '()':
                        print("Processing....")
                        time.sleep(3)
                        print("Processing .....")
                        Face_Detected =False
                        print("No image detected. Please! try again ---")
                        return Face_Detected
                    else:
                        Face_Detected =True
                        imwrite("images/Geeks.jpg", img)
                        faceRecognition(Image1 , Image2)
                        if Similarface==[False]:
                            speaker(UnkownText)
                            sendWhatsAppMsg(UnkownText)
                            print("waiting...")
                            time.sleep(2)
                            print("Printed after 2 seconds.")
                        if Similarface==[True]:
                            print("Result after comparision:"+str(Similarface))
                            speaker(myText)
                            sendWhatsAppMsg(myText)
                            print("waitting...")
                            time.sleep(2)
                            print("Printed after 2 seconds.")
                        os.remove('images/Geeks.jpg')

                    print(faces , Face_Detected)
                    for (x,y,w,h) in faces:
                        # To draw a rectangle in a face 
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
                        roi_gray = gray[y:y+h, x:x+w]
                        roi_color = img[y:y+h, x:x+w]
                        # Detects eyes of different sizes in the input image
                        eyes = eye_cascade.detectMultiScale(roi_gray) 
                        #To draw a rectangle in eyes
                        for (ex,ey,ew,eh) in eyes:
                            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
                        
                
                    # Display an image in a window
                    cv2.imshow('img',img)
                    
                
                    # Wait for Esc key to stop
                    if cv2.waitKey(30) & 0xFF == ord('q'): 
                        break
                    
                # Close the window
                cap.release()
                
                # De-allocate any associated memory usage
                cv2.destroyAllWindows()
           
                

# we have to make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

while(True):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(float(string)) # convert the unicode string to an int
        print(num)
        if(num>0):
           faceDetector()

ser.close()



    




















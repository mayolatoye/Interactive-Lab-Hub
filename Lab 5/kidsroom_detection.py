
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import os


def say(msg):
   os.system(f"""/usr/bin/mplayer -ao alsa:device=hw=1.0 -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={msg}&tl=en" """); 


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


# Load the model
model = tensorflow.keras.models.load_model('kidsroom_model.h5')
# Load Labels:
labels=[]
f = open("kidsroom_labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())

counter = 0 
FEEDBACK_LOOP = 5
while(True):
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    prediction_label = labels[np.argmax(prediction)]
    #print("The kids room is currently:",labels[np.argmax(prediction)])
    
    if (prediction_label=="Moderately"):
      #  playSound()
       print("Kids! your room is currently a little untidy, please go pick up the mess before dinner")
       if (counter % FEEDBACK_LOOP) == 0: 
         say("Kids! your room is currently a little untidy, please go pick up the mess before dinner") 
    elif (prediction_label=="Very"):
      #  playSound()
       print("Kids! your room is currently a very untidy, please go pick up the mess right away")
       if (counter % FEEDBACK_LOOP) == 0: 
         say("Kids! your room is currently a very untidy, please go pick up the mess right away")
    else:
       if (counter % FEEDBACK_LOOP) == 0: 
         say("Kids room looks clear, nothing to report regarding the state of tidyness")   
       print("The kids room is currently:",labels[np.argmax(prediction)])


    counter = counter + 1
    if webCam:
        if sys.argv[-1] == "noWindow":
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()

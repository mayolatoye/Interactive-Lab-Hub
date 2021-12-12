
#!/usr/bin/env python3
import logging 
import sys
import time
import os
import tempfile
import wave
from vosk import Model, KaldiRecognizer
import json
import contextlib
import io
import pygame
pygame.mixer.init()
import cv2, time
import threading


from datetime import datetime
static_back = None

#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import os


def say(msg):
   os.system(f"""/usr/bin/mplayer -ao alsa:device=hw=1.0 -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={msg}&tl=en" """); 

def playSound(fname="./ding.mp3"):
    pygame.mixer.music.load(fname)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

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
model = tensorflow.keras.models.load_model('keras_model.h5')
# Load Labels:
labels=[]
f = open("labels.txt", "r")
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
    
    if (prediction_label=="Happy"):
      #  playSound()
       print("You appear to be happy today")
       if (counter % FEEDBACK_LOOP) == 0: 
         say("You appear to be happy today, tell me do you feel happy sad or neutral?") 
         with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            motion = False
            try :
               os.system(f"arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav {f.name} > /dev/null 2>&1")
               #playSound("./ping.mp3")
               print("recorded voice")
               wf = wave.open(f.name, "rb")
               # if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
               #    print ("Audio file must be WAV format mono PCM.")
               #    exit (1)
               #    print("about tobuild dict")

               voice_model = Model("model")

               Mindful_Dict = {
                  'happy': 'You are a bright and cheerful person stay at peace and enjoy your day...namaste!', 
                  'sad': 'There there do not be sad there is always something to be grateful for', 
                  'neutral': 'Indifference sends out stressors to your system take a deep breath and calm down you have so much to be thankful for'
               }
               print("built dic now decoding dict")
                
               with contextlib.redirect_stdout(None):
                  with contextlib.redirect_stderr(None):
                     rec = KaldiRecognizer(voice_model, wf.getframerate(), " ".join(list(Mindful_Dict.keys())+ ["[unk]"]) )
                     print("decoded dict")


                  data = wf.readframes(4000)
                  partial = ""
                  while True:
                    data = wf.readframes(4000)
                    if len(data) == 0:
                        break


                    if rec.AcceptWaveform(data):
                        pass 
                    else:
                        xx = json.loads(rec.PartialResult())
                        partial = xx.get("partial","") + partial
                        if partial: 
                            print(partial)
                    
                  for key,val in Mindful_Dict.items(): 
                    if key in partial: 
                        say(val) 
            except :
               logger.exception("error for happy")        
                    
            finally:
                os.unlink(f.name) 

    elif (prediction_label=="Sad"):
      #  playSound()
       print("You appear to be sad today")
       if (counter % FEEDBACK_LOOP) == 0: 
         say("You appear to be sad today, tell me do you feel happy sad or neutral?") 
         with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            motion = False
            try :
               os.system(f"arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav {f.name} > /dev/null 2>&1")
               #playSound("./ping.mp3")
               print("recorded voice")
               wf = wave.open(f.name, "rb")
               voice_model = Model("model")

               Mindful_Dict = {
                  'happy': 'You are a bright and cheerful person stay at peace and enjoy your day...namaste!', 
                  'sad': 'There there do not be sad there is always something to be grateful for', 
                  'neutral': 'Indifference sends out stressors to your system take a deep breath and calm down you have so much to be thankful for'
               }
               print("built dic now decoding dict")
                
               with contextlib.redirect_stdout(None):
                  with contextlib.redirect_stderr(None):
                     rec = KaldiRecognizer(voice_model, wf.getframerate(), " ".join(list(Mindful_Dict.keys())+ ["[unk]"]) )
                     print("decoded dict")


                  data = wf.readframes(4000)
                  partial = ""
                  while True:
                    data = wf.readframes(4000)
                    if len(data) == 0:
                        break


                    if rec.AcceptWaveform(data):
                        pass 
                    else:
                        xx = json.loads(rec.PartialResult())
                        partial = xx.get("partial","") + partial
                        if partial: 
                            print(partial)
                    
                  for key,val in Mindful_Dict.items(): 
                    if key in partial: 
                        say(val) 
            except :
               logger.exception("error for sad")        
            finally:
                os.unlink(f.name) 
    elif (prediction_label=="Neutral"):
      #  playSound()
       print("You appear to be indifferent today")
       if (counter % FEEDBACK_LOOP) == 0: 
         say("You appear to be indifferent today, tell me do you feel happy sad or neutral?") 
         with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            motion = False
            try :
               os.system(f"arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav {f.name} > /dev/null 2>&1")
               #playSound("./ping.mp3")
               print("recorded voice")
               wf = wave.open(f.name, "rb")
               voice_model = Model("model")

               Mindful_Dict = {
                  'happy': 'You are a bright and cheerful person stay at peace and enjoy your day...namaste!', 
                  'sad': 'There there do not be sad there is always something to be grateful for', 
                  'neutral': 'Indifference sends out stressors to your system take a deep breath and calm down you have so much to be thankful for'
               }
               print("built dic now decoding dict")
                
               with contextlib.redirect_stdout(None):
                  with contextlib.redirect_stderr(None):
                     rec = KaldiRecognizer(voice_model, wf.getframerate(), " ".join(list(Mindful_Dict.keys())+ ["[unk]"]) )
                     print("decoded dict")


                  data = wf.readframes(4000)
                  partial = ""
                  while True:
                    data = wf.readframes(4000)
                    if len(data) == 0:
                        print("i am breaking at data")
                        break


                    if rec.AcceptWaveform(data):
                        print("I am passing wave form")
                        pass 
                    else:
                        xx = json.loads(rec.PartialResult())
                        partial = xx.get("partial","") + partial
                        if partial: 
                            print(partial)
                    
                  for key,val in Mindful_Dict.items(): 
                    if key in partial: 
                        say(val) 
            except :
               logger.exception("error for neutral")        
                    
            finally:
                os.unlink(f.name) 
    else:
       if (counter % FEEDBACK_LOOP) == 0: 
         say("You are not giving me any vibes as to how you feel, lets talk about it later when you get back home")   
       print("The human is currently:",labels[np.argmax(prediction)])


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


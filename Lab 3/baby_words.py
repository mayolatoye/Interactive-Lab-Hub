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

motion_list = [ None, None ]

def playSound(fname="./ding.mp3"):
    pygame.mixer.music.load(fname)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def say(msg):
    os.system(f"""/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={msg}&tl=en" """); 

def main(): 
    logger.info("starting")
    global static_back



    while True: 
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            motion = False
            try :
                # Capturing vcideo
                video = cv2.VideoCapture(-1)
                check, frame = video.read()
                video.release()
                # Destroying all the windows
                cv2.destroyAllWindows()
                if not check:
                    time.sleep(.5)
                    continue 
                cv2.imwrite("frame.jpg",frame)

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)
                if static_back is None:
                    static_back = gray
                    continue

                cv2.imwrite("grey.jpg",static_back)
                cv2.imwrite("gray.jpg",gray)

                # Difference between static background
                # and current frame(which is GaussianBlur)
                diff_frame = cv2.absdiff(static_back, gray)
                cv2.imwrite("diff.jpg",diff_frame)
            
                # If change in between static background and
                # current frame is greater than 30 it will show white color(255)
                thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
                thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
                # Finding contour of moving object
                cnts,_ = cv2.findContours(thresh_frame.copy(),
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
                for contour in cnts:
                    if cv2.contourArea(contour) < 10000:
                        continue
                    motion = True
                static_back = gray


                if motion:
                    say("motion detected baby is awake")
                else :
                    say("no motion detected baby is asleep")
                    
                playSound()
                os.system(f"arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav {f.name} > /dev/null 2>&1")
                playSound("./ping.mp3")
                
                wf = wave.open(f.name, "rb")
                if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
                    print ("Audio file must be WAV format mono PCM.")
                    exit (1)

                model = Model("model")

                Baby_Dict = {
                    'mama': 'I need a hug', 
                    'oh': 'I need some food', 
                    'dodo': 'I am tired'
                }
                
                with contextlib.redirect_stdout(None):
                    with contextlib.redirect_stderr(None):
                        rec = KaldiRecognizer(model, wf.getframerate(), " ".join(list(Baby_Dict.keys())+ ["[unk]"]) )


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
                    
                for key,val in Baby_Dict.items(): 
                    if key in partial: 
                        say(val) 
                    
            finally:
                os.unlink(f.name) 

if __name__ == "__main__": 
    main()
from flask import Flask, render_template, Response, request
import datetime, time
from flask_cors import CORS
import cv2
import numpy as np
import threading, queue
import os
import tensorflow.keras
import numpy as np
import pprint
import random 
start_smile_exerice = threading.Event()
smile_detected = threading.Event()

def say(msg):
   os.system(f"""/usr/bin/mplayer -ao alsa:device=hw=1.0 -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={msg}&tl=en" """); 


q = queue.Queue()

global capture,rec_frame, grey, neg, face, rec, out , face_detected, current_frame, mood, smile 

capture=0
grey=0
neg=0
face=1
rec=0
mood = None
face_detected= False
smile = None 

net = cv2.dnn.readNetFromCaffe('./deploy.prototxt.txt', './res10_300x300_ssd_iter_140000.caffemodel')
model = tensorflow.keras.models.load_model('keras_model.h5')

# Load Labels:
labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())

app = Flask(__name__)
CORS(app)

camera = None


def smile_exerices():
    global smile  
    count = 0
    total = 5

    images = [
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/cat_meme.jpeg",
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/cat_meme2.jpeg",
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/covid_meme.webp",
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/zoom_meme.jpeg",
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/6.png",
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/7.png",
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/8.png",    
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/9.png",    
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/10.png",    
    ] 

    completed_images = [
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/1.png",
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/2.png",
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/3.png",    
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/4.png",    
        "https://raw.githubusercontent.com/mayolatoye/Interactive-Lab-Hub/Fall2021/Lab%206/images/5.png",    
    ] 
    while True:
        print("Monitoring for face detect")
        x = start_smile_exerice.wait()
        imgs = random.sample(images, k=4)
        total= len(imgs)
        count = 0

        print("face detected")
        url = imgs[0]
        smile = {
                "msg": "Keep working those smile muscles",
                "img_url": url,
                "progress": 0
        }

        for x in range(total): 
            url = imgs[x]
            print("wait for happy")
            smile_detected.wait()
            smile["img_url"] =  url
            smile["progress"] = (count / total) * 100.0
        
            pprint.pprint(smile)
            count = count + 1
            smile_detected.clear()
            print("pause for question ")
            time.sleep(5)
            print("clear for question ")
        
        start_smile_exerice.clear() 
        smile["msg"] = "great job" 
        smile["img_url"] =  random.choice(completed_images)
        smile["progress"] = 100
        time.sleep(10)
        smile= None
        time.sleep(10)

        print("restart for question ")

def audio_service():
    import os
    while True:
        msg = q.get()
        print(msg)
        # os.system(f"""/usr/bin/mplayer -ao alsa:device=hw=1.0 -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={msg}&tl=en" """); 
        q.task_done()     

def video_stream():
    global out, capture,rec_frame, current_frame
    while True:
        success, frame = camera.read() 
        if success:
            if(face):  
                confi= detect_face(frame)
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                current_frame = buffer.tobytes()
            except Exception as e:
                pass
        else:
            pass


@app.before_first_request
def init():
    global camera

    if camera: 
        camera.release()
    cv2.destroyAllWindows()    

    camera = cv2.VideoCapture(0, cv2.CAP_V4L)
    threading.Thread(target=video_stream, daemon=False).start()
    threading.Thread(target=audio_service, daemon=False).start()
    threading.Thread(target=smile_exerices, daemon=False).start()

def detect_face(frame):
    global net, face_detected, mood
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 123.0))   
    net.setInput(blob)
    detections = net.forward()
    confidence = detections[0, 0, 0, 2]
    face_detected_old = face_detected
    face_detected = confidence > .6

    if face_detected:
        start_smile_exerice.set()
        rows, cols, channels = frame.shape
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        size = (224, 224)
        img =  cv2.resize(frame, size, interpolation = cv2.INTER_AREA)
        #turn the image into a numpy array
        image_array = np.asarray(img)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference
        prediction = model.predict(data)
        prediction_label = labels[np.argmax(prediction)]

        if prediction_label == "Happy" :
            smile_detected.set()
        print(prediction_label)
            
        mood = prediction_label
    else:
        mood = None

    if not face_detected_old and face_detected: 
        q.put("Hello there, what do you think of this meme?")


    return confidence           

@app.route('/')
def index():
    global  face_detected, mood, smile
    return {
        "face_detected": bool(face_detected),
        "smile" : smile,
        "msg": "Namaste Dear Friend!",
        "mood": mood,
        "img_url": f"https://source.unsplash.com/random/400x300?person&t={datetime.datetime.now().timestamp()}"
    }


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen_frames():  # generate frame by frame from camera
    global current_frame
    while True:
        try:

            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + current_frame + b'\r\n')

            time.sleep(1)
        except Exception as e:
            pass



if __name__ == '__main__':
    app.run(host="0.0.0.0")

if camera:
    camera.release()
cv2.destroyAllWindows()    
q.join()
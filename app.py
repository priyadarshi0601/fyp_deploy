import json,time,base64
#from camera import VideoCamera
from flask import Flask,render_template,jsonify,Response
from flask import request
import numpy as np
from io import BytesIO
from PIL import Image
import base64,cv2
import cv2

import numpy as np
import keras
import dlib
from tensorflow.keras import layers
from PIL import Image
from imutils import face_utils 
import numpy as np 
import argparse 
import imutils 
import dlib 
import pandas as pd
from imutils.video import WebcamVideoStream

app=Flask(__name__)
output=[]

detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
cnn_model=keras.models.load_model('1dcnnv2.h5')
output=""
@app.route('/')
def home():
    return render_template("test.html",result=output)
@app.route('/',methods = ['POST', 'GET'])
def video():
    try:
        global output
        if request.method == 'POST':
            # print("Image recieved")
            # print('THE DETECTOR IS',detector)
            data_url = request.values['imageBase64']
            #print(data_url)
            pp=data_url[21:]
            res = bytes(pp, 'utf-8')
            # Decoding base64 string to bytes object
            img_bytes = base64.b64decode(res)
            img = Image.open(BytesIO(img_bytes))
            img.convert('RGB').save('geeks.jpg')
            img=cv2.imread('geeks.jpg')
            #print(type(img))
            print(np.array(img).shape)   
            d={0:'Angry',1:'Fear',2:'Happiness',3:'Neutral',4:'Sadness',5:'Surprise'}
            t=''
            rects=detector(img,1)
            print(len(rects))
            if(len(rects)>0):
                rects=rects[0]
                #print('ll')
                shape = predictor(img, rects) 
                shape = face_utils.shape_to_np(shape)
                #print(shape.shape)
                pix = np.expand_dims(shape, axis=0)
                trr=cnn_model.predict(pix)
                trr=[i for i in trr[0]]
                t=d[trr.index(max(trr))]
                print(t)
                output=t
        return output 
    except:
        print('KI holo')

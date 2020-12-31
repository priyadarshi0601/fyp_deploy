import json,time
from camera import VideoCamera
from flask import Flask,render_template,jsonify,Response
import requests
import base64,cv2
import cv2
import cv2
from PIL import Image
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
import cv2
import pandas as pd
from imutils.video import WebcamVideoStream

app=Flask(__name__)
output=[]
@app.route('/')
def home():
    return render_template("home.html",result=output)
@app.route('/about')
def about():
    return render_template("about.html",result=output)
def gen(camera,m,d,p):
    while True:
        data=camera.get_frame(m,d,p)
        frame=data[0]
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    cnn_model=keras.models.load_model(r'C:\Users\Priyadarshi 2019\Downloads\1dcnnv2.h5')
    detector = dlib.get_frontal_face_detector()
    predictor=dlib.shape_predictor(r"C:\Users\Priyadarshi 2019\Downloads\shape_predictor_68_face_landmarks.dat")
    print('pp')
    return Response(gen(VideoCamera(),cnn_model,detector,predictor), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=="__main__":
    app.run(debug=True)
import json,time
from camera import VideoCamera
from flask import Flask,render_template,jsonify,Response
import requests
import base64,cv2

app=Flask(__name__)
output=[]
@app.route('/')
def home():
    return render_template("home.html",result=output)
@app.route('/about')
def about():
    return render_template("about.html",result=output)
@app.route('/cam')
def gen(camera):
    while True:
        data=camera.get_frame()
        frame=data[0]
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')
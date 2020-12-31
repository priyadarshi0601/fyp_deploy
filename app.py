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
def camera1():
    return render_template("camera.html")



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
class VideoCamera(object):
    def __init__(self):
        self.stream=WebcamVideoStream(src=0).start()
        
    def __del__(self):
        self.stream.stop()
    def get_frame(self,cnn_model,detector,predictor):
        image=self.stream.read()
        #print(image.shape)
        ret,jepg=cv2.imencode('.jpg',image)
        data=[]
        data.append(jepg.tobytes())     
        d={0:'Angry',1:'Fear',2:'Happiness',3:'Neutral',4:'Sadness',5:'Surprise'}
        t=''
        im=image
        #print(type(im))
        rects=detector(im,1)
        if(len(rects)>0):
            rects=rects[0]
            #print('ll')
            shape = predictor(im, rects) 
            shape = face_utils.shape_to_np(shape)
            #print(shape.shape)
            pix = np.expand_dims(shape, axis=0)
            trr=cnn_model.predict(pix)
            #print(trr)
            trr=[i for i in trr[0]]
            #print(max(trr),trr.index(max(trr)))
            t=d[trr.index(max(trr))]
            print(t)
        return data

    

    
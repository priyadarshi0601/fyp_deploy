import cv2
from imutils.video import WebcamVideoStream
class VideoCamera(object):
    def __init__(self):
        self.stream=WebcamVideoStream(src=0).start()
    def __del__(self):
        self.stream.stop()
    def get_frame(self):
        image=self.stream.read()
        print(type(image))
        
        ret,jepg=cv2.imencode('.jpg',image)
        data=[]
        data.append(jepg.tobytes())
        return data
    

    
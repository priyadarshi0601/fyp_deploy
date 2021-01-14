  
from flask import Flask,render_template,jsonify,Response
import requests

app=Flask(__name__)
output=[]
@app.route('/')
def home():
    return render_template("test.html",result=output)
if __name__=="__main__":
    app.run(debug=True)

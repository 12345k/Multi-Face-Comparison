from flask import Flask, render_template ,request, send_from_directory,Response
from flask import jsonify
import json
import re
import os
import scipy.misc
import warnings
import sys
import compare_image
import time
import detect_face
from werkzeug.utils import secure_filename

app = Flask(__name__)
 


@app.route('/api/v1/compare_faces', methods=['POST'])
def compare_faces():
    target = request.files['target']
    faces =  request.files.getlist("faces")
    target_filename=secure_filename(target.filename)
    response=[]
    for face in faces:
        start = time.time()
        distance,result = compare_image.main(target,face)
        end=time.time()
        json_contect={
                'result':str(result),
                'distance':round(distance,2),
                'time_taken':round(end-start,3),
                'target':target_filename,
                'face':secure_filename(face.filename)
            }
        response.append(json_contect)
    python2json = json.dumps(response)
    return app.response_class(python2json, content_type='application/json') 



@app.route('/api/v1/detect_faces', methods=['POST'])
def detect_faces():
    faces =  request.files.getlist("faces")
    # target_filename=secure_filename(target.filename)
    response=[]
    for face in faces:
        start = time.time()
        _,result = detect_face.get_coordinates(face)
        end=time.time()
        json_contect={
                'coordinates':result,
                'time_taken':round(end-start,3),
                'image_name':secure_filename(face.filename)
            }
        response.append(json_contect)
    python2json = json.dumps(response)
    return app.response_class(python2json, content_type='application/json') 

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)
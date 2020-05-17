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
from werkzeug.utils import secure_filename

app = Flask(__name__)
 


@app.route('/api/v1/compare_faces', methods=['POST'])
def upload_file():
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
                'distance':distance,
                'time_taken':str(end-start),
                'target':target_filename,
                'face':secure_filename(face.filename)
            }
        response.append(json_contect)
    python2json = json.dumps(response)
    return app.response_class(python2json, content_type='application/json') 

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)
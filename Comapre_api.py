from flask import Flask, render_template ,request, send_from_directory
from flask import jsonify
import json
import re
import os
import re
import scipy.misc
import warnings
import face_recognition.api as face_recognition
import sys
import compare_image
import time
app = Flask(__name__)
 


@app.route('/upload', methods=['POST'])
def upload_file():
	t1=time.time()
	print (request.files)
	# checking if the file is present or not.
	# if 'file' not in request.files:
	# 	return "No file found"
	
	img_1 = request.files['img_1']
	img_2 = request.files['img_2']

	distance,result = compare_image.main(img_1,img_2)
	
	# file.save("static/test.jpg")
	t1=time.time()-t1
	json_contect={
					'result':str(result),
					'distance':distance,
					'time_taken':str(t1)
				}
	python2json = json.dumps(json_contect)
	return app.response_class(python2json, content_type='application/json') 
		
	
if __name__ == "__main__":
    app.run(debug=True)
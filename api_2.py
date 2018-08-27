from flask import Flask, render_template ,request
from flask import jsonify
import json
import re

app = Flask(__name__)
 


@app.route('/predict', methods=['POST'])
def make_prediction():
	if str(request.method)==str('POST'):
		content = request.get_json(silent=True)
		print(content)

		email_text = content['email_text']
		subject_text = content['subject_text']

		full_text= subject_text + email_text

		kyc_target_text=[
						 "kyc","aadhar" ,"PAN","bank","electricity", 
						 "bill" ,"rent","card","passport","visa"
						]
		
		shiptrack_target_text=[
								"shiptack","number","delivery","track","shipment",
								"time","packages","transporting","logistic","status"
							  ]
        
		kyc_count=0
		for i in kyc_target_text:
			kyc_count+=full_text.count(i)

		
		shiptrack_count=0
		for i in shiptrack_target_text:
			shiptrack_count+=full_text.count(i)

		if kyc_count > shiptrack_count:
			json_contect={
						  'mail':'datalabs_kyc@optisolbusiness.com',
						  'phone_number':""
						 }
			python2json = json.dumps(json_contect)
			return jsonify(python2json)
		else:
			regexp="(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
			phone = re.findall(regexp, full_text)
			json_contect={
						  'mail':'datalabs_shiptrack@optisolbusiness.com',
						  'phone_number':phone
						 }
			python2json = json.dumps(json_contect)
			return jsonify(python2json)

		
		
	
if __name__ == "__main__":
    app.run(debug=True)
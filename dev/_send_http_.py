

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import conf

# pip install requests-toolbelt

# Define your form data
def snet_data(WATER,RAIN,STAT):
	c = conf.TEST_SITE_COORDS
	params = {
			"filename": conf.SERIAL_NUM,
			"name": conf.TEST_SITE_CNAME,
			"device": "",
			"latlong": "{},{}".format(c[0],c[1]),
			"num": str(RAIN),
			"emer_num": str(WATER),
			"status": "{}::0.0004124999977648258__0__0.0002749999985098839".format(STAT)
		}

	data = MultipartEncoder(fields=params)
	print(type(data))
	headers = {'Content-type': data.content_type}

	response = requests.post('http://localhost:5000/rain/set_users/{}'.format(params['filename']), data=data, headers=headers)
	# response = requests.post('https://wilmar1995.pythonanywhere.com/rain/set_users/{}'.format(data['filename']), data=data, headers=headers)
	print(response.text)

snet_data(1,1.1,"idele")
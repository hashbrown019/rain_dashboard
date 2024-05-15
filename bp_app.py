from datetime import date, datetime
from flask import Blueprint, render_template, request, session, redirect, jsonify, Response,send_file
from flask_session import Session
from modules.Connections import mysql,sqlite
import Configurations as c
import os, random, json, shutil, base64, sys, warnings, csv, xlrd
from werkzeug.utils import secure_filename
from flask_cors import CORS,cross_origin

import pandas as pd
from tqdm import tqdm

app = Blueprint("rain",__name__,template_folder='pages')
rapid_mysql = mysql(*c.DB_CRED)

# JSON_PATH = "assets/response/devices.json"
# app = Flask(__name__)
@app.route("/rain")
@app.route("/rain/dashboard")
def dashboard():
	return render_template('ft_index.html')


@app.route("/home")
def home():
	return redirect("/rain/dashboard")


@app.route("/rain/get_all_status",methods=["POST","GET"])
def get_all_status():
	all_users = {}
	# _file = open(c.JSON_PATH,"r")
	# _data = _file.read()
	for fname in os.listdir(c.JSON_PATH):
		try:
			_file = open(c.JSON_PATH+fname,"r")
			_data = json.loads(_file.read())
			all_users[fname] = _data
		except Exception as e:
			pass
	return jsonify(all_users)
	# return jsonify(_data)


@app.route("/rain/set_users/<name>",methods=["POST","GET"])
def set_users(name):
	user = {}
	for key in request.form:
		user[key] = request.form[key]
	_file = open(c.JSON_PATH+name,"w")
	_data = _file.write(json.dumps(user))
	_file.close()
	return "DONE"

@app.route("/dl/<file_>",methods=["POST","GET"])
def download_file(file_):
	# today = str(datetime.today()).replace("-","_").replace(" ","_").replace(":","_").replace(".","_")
	# def_name = "{}_{}".format(today,file_)
	def_name = file_
	return send_file(file_, as_attachment=True,download_name=def_name)

@app.route("/clear",methods=["POST","GET"])
def clear():
	folder = c.JSON_PATH
	for filename in os.listdir(folder):
		file_path = os.path.join(folder, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))
	return redirect("/rain/dashboard")


@app.route("/login/<pass_>",methods=["POST","GET"])
def login(pass_):
	folder = c.LOGIN_PATH
	try:
		open(folder+pass_,"r")
		return redirect("/rain/dashboard")
	except Exception as e:
		return redirect("/home")
		# raise e


@app.route("/ch_pass/<pass_>",methods=["POST","GET"])
def ch_pass(pass_):
	folder = c.LOGIN_PATH
	for filename in os.listdir(folder):
		file_path = os.path.join(folder, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))
		# raise e
	f = open(folder+pass_,"w")
	f.close()

	return redirect("/home")
	

# ======================================
_data_struct = [
	{
		"name" : "",
		"device" : "",
		"latlong" : "",
		"num" : "",
		"emer_num" : "",
		"accel" : "",
		"gyro" : "",
		"axis" : "",
		"status" : ""
	}
]
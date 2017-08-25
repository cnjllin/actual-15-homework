#!/usr/bin/env python 
# File Name: run.py
# Author: luofeng
# Mail: 18210085737@139.com 
# Blog: https://www.liyanlan.com 
# _*_ coding: utf-8 _*_

from flask import *
app = Flask(__name__)

def check_user_state(username):
	match_flags = False
	with open('user_information.txt','rb') as f:
		for user_info in f.readlines():
			user,phone,passwd  = user_info.strip().split(':')	
			if username == user:
				match_flags = True
				return match_flags 

@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/regis/",methods=['GET','POST'])
def regis():
	if request.method == 'POST':
		username = request.form.get('fullname')
		if check_user_state(username) == True:
			return "User {0} is exist.".format(username)
		else:
			phone = request.form.get('phone_num')
			password = request.form.get('password')
			with open('user_information.txt','ab') as f:
				f.write('{0}:{1}:{2}\n'.format(username,phone,password))
				return render_template('success.html',username=username,phone=phone)

	return render_template('regis.html')

@app.route("/login/",methods=['GET','POST'])
def login():
	if request.method == 'POST':
		phones = request.form.get('phone')
		password = request.form.get('password')
		with open('user_information.txt','rb') as f:
			message = []
			for line in f.readlines():
				phone = line.strip().split(':')[1]
				passwd = line.strip().split(':')[2]
				message.append((phone,passwd))
			
			for k in message:
				if k[0] == phone and k[1] == password:
					nginx_log = nginx_counts()
					return render_template('login.html', phone=phones, nginx_log=nginx_log)
				else:
					return render_template('error.html',)

@app.route("/nginx_counts/")
def nginx_counts():
	counts = {}
	with open('access.txt','rb') as f:
		for line in f.readlines():
			cip = line.strip().split(' ')[0]
			url = line.strip().split(' ')[6]
			status = line.strip().split(' ')[8]
			counts[cip,url,status] = counts.get((cip,url,status),0) + 1
	
	result = [] 
	for log in sorted(counts.items(), key=lambda key:key[1],reverse=True)[:10]:
		ip = log[0][0]
		url = log[0][1]
		status = log[0][2]
		count = log[1]
		result.append((ip,url,status,count))

	result_key = [('ip',1),('url',2),('status',3),('count',4)]
	result_list = []
	for key in result:
		row = {}
		for i in range(len(result_key)):
			row[result_key[i][0]] = key[i]
		result_list.append(row)
	return result_list

if __name__ == "__main__":
 app.run(
 host="0.0.0.0",
 port=8080,
 debug=True)

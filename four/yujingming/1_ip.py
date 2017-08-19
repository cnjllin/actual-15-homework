#!/usr/bin/env python
#coding:utf-8


from flask import Flask,render_template

app = Flask(__name__)

# 将文件里的数据取出来，处理成列表，通过render_template及jinja2将数据在前端HTML渲染
@app.route('/index/')
@app.route('/')
def index():
	dic = {}
	with open('access.txt') as f:
		logs = f.readlines()
		for line in logs:
			ip = line.split()[0]
			if ip in dic:
	 			dic[ip] += 1
			else:
				dic[ip] = 1

	def getOrderKey(x):
		return x[1]
	list = sorted(dic.items(),key =getOrderKey,reverse=True)[:10]

	return  render_template('index.html',list=list)
if __name__ =='__main__':
	app.run(host='0.0.0.0', port=8888,debug=True)

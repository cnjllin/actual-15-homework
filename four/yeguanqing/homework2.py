#!/usr/bin/env python
#coding:utf-8
'''
处理nginx的日志文件，取TOP10的IP地址以及次数；
将文件里的数据取出来，处理成列表，通过render_template及jinja2将数据在前端HTML渲染
'''


from flask import Flask,render_template

app = Flask(__name__)

# 将文件里的数据取出来，处理成列表，通过render_template及jinja2将数据在前端HTML渲染
@app.route('/index')

def index():
	nginxip = {}
	with open('access.txt') as f:
    		logs = f.readlines()
		for line in logs:
    			ip = line.split()[0]
    			if ip in nginxip:
       		 		nginxip[ip] += 1
   			else:
        			nginxip[ip] = 1

	list = sorted(nginxip.iteritems(),key=lambda x:x[1],reverse=True)[:10]

	return  render_template('index.html',list=list)
if __name__ =='__main__':
	app.run(host='0.0.0.0', port=6666,debug=True)

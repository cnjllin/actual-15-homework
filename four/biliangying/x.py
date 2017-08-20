#!/usr/bin/python
#coding:utf-8
from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/reg/',methods=['GET','POST'])
#注册
def register():
	f=open('a.txt','a+')
	a = []
	for i in f.readlines():
		a.append(i.split(':')[0])
	if request.method=="POST":
		username = request.form.get('username')
		if username in a:
			return '用户存在'
		else:
			passwd1 = request.form.get('passwd1')
			passwd2 = request.form.get('passwd2')
			if passwd1 == passwd2:
				f.write("%s:%s\n" % (username,passwd1))
				f.close()
				return render_template('login.html')
			else:
				return "密码不一致"
	return render_template('register.html')
#登录
@app.route('/log/',methods=['GET','POST'])
def login():
	f=open('a.txt')
        a=[]
        b={}
        for i in f.readlines():
		a.append(i.strip('\n').split(':'))
        for j in a:
                b[j[0]]=j[1]
	if request.method=="POST":
        	username = request.form.get('username')
		if username in b.keys():
			passwd = request.form.get('passwd')
		else:
			print "用户不存在"
		if passwd == b[username]:
			return render_template('nginx.html')
		else:
			return "密码不对"	
	return render_template('login.html')
#日志top10
@app.route('/hehe/')
def ip():
        from collections import defaultdict
        fo = open('access.txt')
        a = []
        b = {}
        for i in fo.readlines():
                a.append( (i.split(' ')[0],i.split(' ')[6],i.split(' ')[8]))
        b = defaultdict(int)
        for j in a:
                b[j] += 1
        b=sorted(b.items(),key=lambda item:item[1],reverse=True)[0:10]
        #for x in b:
                #y = (list(x))
        return render_template("nginx.html",b=b)
if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5550,debug=True)

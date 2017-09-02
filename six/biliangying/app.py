#!/usr/bin/python
#coding:utf-8
from flask import Flask,request,render_template,redirect
import utils
app = Flask(__name__)
# 首页
@app.route('/')
@app.route('/index/')
def index():
	username = "wd"
	return render_template('index.html',username=username)

# 注册
@app.route('/reg/',methods=['GET','POST'])
def register():	
	field=[]
	data=[]
	if request.method=="POST":
		user = {k:v[0] for k,v in dict(request.form).items()}
		print user
		if len(user["username"].strip()) == 0:
			return render_template('register.html',errmsg1=u"用户名不能为空")
		result = utils.judgeuser(user)
		if result["code"] == 0:
			return render_template('register.html',errmsg1=u"用户名存在")
		else:
			if len(user["password"].strip()) < 6:
				return render_template('register.html',errmsg2=u"密码不得小于6位")
			elif user["password"] != user["repassword"]:
				return render_template('register.html',errmsg2=u"密码不一致")
			else:
				del user['repassword']
				for k,v in user.items():
                        		field.append(k)
                        		data.append("'%s'" % v)
				utils.insert(field,data)
				return redirect('/login/')
	return render_template('register.html')

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method=="POST":
		user = {k:v[0] for k,v in dict(request.form).items()}
		result = utils.judgeuser(user)
		if result["code"] == 0:
			res = utils.login(user)
			role = utils.role(user)
			print role
			if res['code'] == 0 and role['code'] == 0:
				return redirect('/list/')
			elif res['code'] == 0 and role['code'] == 1:
				return redirect('/getone/')
			else:
				return render_template('login.html',errmsg2=u"密码错误")
		else:
			return render_template('login.html',errmsg1=u"用户不存在")
        return render_template('login.html')

# 用户列表
@app.route('/list/')
def list():
	user = utils.userlist()
	return render_template('list.html',user=user)

# 普通用户
@app.route('/getone/')
def getone():
	return render_template('getone.html')

# 删除
@app.route('/delete/',methods=['GET','POST'])
def delete():
	if request.method=="GET":
		uid = request.args.get('id','')
		utils.delete(uid)
		return redirect('/list/')
	return render_template('list.html')

# 更改
@app.route('/update/',methods=['GET','POST'])
def update():
	if request.method=="GET":
		uid = request.args.get('id','')
		user = utils.inquire(uid)
		return render_template('update.html',user=user)
	if request.method=="POST":
		user = {k:v[0] for k,v in dict(request.form).items()}	
		print user
		utils.update(user)
		return redirect('/list/')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5555,debug=True)

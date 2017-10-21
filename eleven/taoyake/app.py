#/usr/bin/python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask,render_template,request,redirect,session,json
import MySQLdb as mysql
from utils import insert,getone,getlist,update,drop


app = Flask(__name__)

app.secret_key="dsadfasfadsfasf"
field = ['id','username','password','age','phone','email','role']


# 首页,超链接一个注册和登录的页面
@app.route('/')
@app.route('/index')
def index():
    home = '欢迎访问首页!'
    return render_template('index.html',home = home)

# 用户注册
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user = {k:v[0] for k,v in dict(request.form).items()}
        print user
        #field = ['username','password','role']
        field = ['username','password','age','phone','email','role']
        result = insert('user',field,user)
        if result['code'] == 0:
            return redirect('/userlist/')
        else:
            return render_template("register.html",result = result)
    return render_template("register.html")

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        result = getone('user',field,data)
        if result['code'] == 0:
            if result['msg']['password'] == data['password']:
                session['username'] = data['username']
                session['role'] = result['msg'] ['role']
                print session
                if session['role'] == 0:
                    return json.dumps(result)
                else:
                    return redirect('/')
            else:
                result['msg']="user exist,but password is error"
        else:
            result['msg'] = "user is not exist!"
            return render_template("login.html",result = result)
    return render_template("login.html")

@app.route('/userlist/')
def userlist():
    if session:
        result = getlist('user',field)
        print result
        return render_template('userlist.html',result=result)
    else:
        return redirect('/')

@app.route('/logout/')
def logout():
    if session:
        session.clear()
    return redirect("/login/")

@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect("/login")
    uid = request.args.get("id","")
    data = {'id':uid}
    result = getone('user',field,data)
    print result
    if result['code'] == 0:
        result = result['msg']
    #return json.dumps(result)
    return render_template("update.html",result=result)

# 更新
@app.route('/update/',methods=['GET','POST'])
def modify():
    
    if request.method == 'GET':
        uid = request.args.get("id","")
        data = {'id':uid}
        result = getone('user',field,data)
        print result
        if result['code'] == 0:
            result = result['msg']
        return json.dumps(result)
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        result = update('user',field,data)
        print result
        if result['code']==0:
            return  json.dumps(result)
        else:
            return render_template('update.html',result=result)
    #return render_template("update.html",) 
@app.route('/delete/')
def delete():
    if request.method == 'GET':
        id = int(request.args.get('id'))
        print id
        sql = 'delete from user where id=%d;' % id
        print sql
        if drop(id, sql):
            return redirect('/userlist/')

# 增加用户信息
@app.route('/adduser/',methods=['GET','POST'])
def add_user():
        if request.method == 'POST':
                user_dict = {k:v[0] for k,v in dict(request.form).items()}
                print user_dict
                field = ['username','password','age','phone','email','role']
                result = insert('user',field,user_dict)
                print result
                if result['code'] == 0:
                        return json.dumps(result)
        return render_template('adduser.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5566,debug=True)

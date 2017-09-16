# -*- coding: utf-8 -*-
import MySQLdb as mysql
from flask import Flask,render_template,request,session,redirect
import json
import util2
db=mysql.connect(host="192.168.62.1",user="root",passwd="zhaoxf513",db="reboot15",port=3306,charset='utf8')
db.cursor()
cur = db.cursor()
app = Flask(__name__)
app.secret_key = 'sadaredfs'
table = 'user'
field = ['id', 'username', 'password', 'role']
app = Flask(__name__)


@app.route('/logout/')
def logout():
    if session:
        session.clear()
        return redirect('/login/')
    else:
        return redirect('/login/')


@app.route('/')
def hello_world():
    if not session:
        return redirect('/login/')
    else:
        return render_template('hello world.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        name = data.get('username', '')
        passwd = data.get('password', '')
        result = util2.logincheck(name,passwd)
        if result['code'] == 1:
            session['username'] = result['username']
            session['role'] = result['role']
            session['id'] = result['id']
            return json.dumps(result)
    else:
        return render_template("login.html")

@app.route('/register/',methods=['GET','POST'])
def register():
    if not session:
        reg_info = {}
        if request.method == 'GET':
            return render_template('register.html', reg_info=reg_info)
        else:
            table_name = 'user'
            dict_reg = dict((k, v[0]) for k, v in dict(request.form).items())
            print dict_reg
            reg_info = util2.usercheck(table_name, **dict_reg)
            if reg_info['code'] == 1:
                return redirect('/login/')
            else:
                return render_template("register.html",result=reg_info)
    else:
        return redirect('/')

@app.route('/userlist/')
def userlist():
    if session:
        if session['role'] ==1:
            user_dict = util2.admlist()
            return render_template('userlist.html', result=user_dict)
        else:
            name = session['username']
            user_dict = util2.getone(name)
            return render_template('userlist.html', result=user_dict)
    else:
        return redirect('/login/')

@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect('/login/')
    else:
        uid = request.args.get('id')
        user_dict = {'id': uid}
        result = userinfo(user_dict)
        print result
        if result['code'] == 1:
            return json.dumps(result)



if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5001)

# -*- coding: utf-8 -*-
import MySQLdb as mysql
from flask import Flask,request,render_template,redirect,session,json
import util2
db=mysql.connect(host="192.168.50.160",user="root",passwd="zhaoxf513",db="reboot15",port=3306,charset='utf8')
db.cursor()
cur = db.cursor()
app = Flask(__name__)
app.secret_key = 'sadaredfs'
table = 'user'
field = ['id', 'username', 'password', 'role']



@app.route('/logout/')
def logout():
    if session:
        session.clear()
    return redirect('/signin')


@app.route('/')
@app.route('/index/')
def index(username=''):
    if not session:
        return redirect('/signin')
    else:
        return render_template('homepage.html', username=username)

@app.route('/signup/',methods=['POST','GET'])
def reg():
    reg_info = {}
    if request.method == 'GET':
        return render_template('signup.html',reg_info=reg_info)
    else :
        table_name = 'user'
        dict_reg = dict((k,v[0]) for k,v in dict(request.form).items())
        reg_info = util2.usercheck(table_name,**dict_reg)
        if reg_info['code'] == 1:
            return redirect('/signin/')
        else:
            return render_template('signup.html', reg_info=reg_info)

@app.route('/signin/',methods=['POST','GET'])
def login():
    login_message = {'code':'0','msg':''}
    if request.method == 'GET':
        return render_template('login_submit.html',login_message = login_message)
    else :
        dict_login = dict((k,v[0]) for k,v in dict(request.form).items())
        name = dict_login.get('username', '')
        passwd = dict_login.get('password', '')
        login_message = util2.logincheck(name, passwd)
        if login_message['code'] == 1:
            session['username'] = login_message['username']
            session['role'] = login_message['role']
            session['id'] = login_message['id']
            return redirect("/userlist/")
        else:
            return render_template('login_submit.html',login_message=login_message)

@app.route('/userlist/')
def userlist():
    if session:
        if session['role'] ==1:
            user_dict = util2.admlist()
            return render_template('userlist.html', userdict=user_dict)
        else:
            name = session['username']
            user_dict = util2.userdata(name)
            return render_template('userlist.html', userdict=user_dict)
    else:
        return redirect('/signin/')


@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect('/signin/')
    else:
        uid = request.args.get('id','')
        print uid
        data = {'id':uid}
        info_dict = util2.userinfo(data)
        print info_dict
        if info_dict['code'] == 1:
            # return json.dump(info_dict)
            return render_template('update.html', result=info_dict)
        else:
            return redirect('/userlist/')


@app.route('/update/',methods=['POST','GET'])
def update():
    if session:
        if request.method == 'POST':
            data = dict(request.form)
            data = {k: v[0] for k, v in data.items()}
            print data
            result = util2.update(data)
            print result
            if result['code'] == 0:
                return redirect("/userlist/")
            else:
                return render_template('update.html', result=result)
    else:
        return redirect('/signin/')

@app.route('/delete/', methods=['GET', 'POST'])
def delete():
    if not session:
        return redirect('/signin/')
    else:
        if request.method == 'GET':
            uid = request.args.get('id', '')
            data = {'id': uid}
            res = util2.delete('user', data)
            print session['id'],uid
            if session['id'] == uid :
                return redirect("/logout/")
            else:
                return redirect("/userlist/")














if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9999, debug=True)















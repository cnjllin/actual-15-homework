# -*- coding: utf-8 -*-
import MySQLdb as mysql
from flask import Flask,request,render_template,redirect
import util2
db=mysql.connect(host="192.168.50.160",user="root",passwd="zhaoxf513",db="reboot15",port=3306,charset='utf8')
db.cursor()
cur = db.cursor()
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index(username=''):
    return render_template('homepage.html',username=username)

@app.route('/signup/',methods=['POST','GET'])
def reg():
    reg_info = {}
    dict_reg = {}
    if request.method == 'GET':
        return render_template('signup.html',reg_info=reg_info,user_dict=dict_reg)
    else :
        dict_reg = dict((k,v[0]) for k,v in dict(request.form).items())
        reg_info = util2.usercheck(**dict_reg)
        return render_template('signup.html',reg_info=reg_info)

@app.route('/signin/',methods=['POST','GET'])
def login():
    login_message = {'code':'0','msg':''}
    dict_login = {}
    if request.method == 'GET':
        return render_template('login_submit.html',login_message = login_message)
    else :
        dict_login = dict((k,v[0]) for k,v in dict(request.form).items())
        name = dict_login.get('username', '')
        passwd = dict_login.get('password', '')
        sql = "select username,password from user;"
        login_message = util2.logincheck(name, passwd,sql)
        if login_message['code'] == 1:
            userlist(name)
            return redirect("/userlist/")
        else:
            return render_template('login_submit.html',login_message=login_message)

@app.route('/userlist/')
def userlist(name):
    sql_ch = "select role from user where username = '%s';" % name
    user_role = util2.admcheck(sql_ch)
    if user_role == 1:
        sql_list = "select * from user;"
        list_adm = util2.admlist(sql_list)
        role = 'nobody'
        return render_template('admlist.html', list_adm=list_adm, role=role)
    else:
        sql = "select * from user where username = '%s';" % name
        user_dict = util2.userlist(sql)
        update(**user_dict)
        role = 'nobody'
        return render_template('userlist.html', userdict=user_dict, role=role)

@app.route('/update/', methods=['POST', 'GET'])
def update(**user_dict):
    print user_dict
    msg = ''
    usname = user_dict.get('username', '')
    id = user_dict.get('id', '')
    if request.method == 'GET':
        return render_template('update.html', username=usname,msg=msg)
    else :
        user_data = dict((k, v[0]) for k, v in dict(request.form).items())
        sql_update = "UPDATE user set password='%s' where id='%s';" % (user_data['password'],id)
        msg = util2.update(sql_update,id)
        return render_template('update.html', user_dict=user_dict,msg=msg)

@app.route('/delete/', methods=['POST', 'GET'])
def delete():
    if request.method == 'GET':
        return render_template('delete.html',msg='')
    else:
        username = request.form.get('username','')
        sql = "select id from user where username = '%s';" % username
        msg = util2.delete(sql)
    return render_template('delete.html',msg=msg)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9999, debug=True)
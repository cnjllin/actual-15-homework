#coding:utf-8
from flask import render_template,redirect,session,request,url_for
from apps import app
import dbutils
import datetime,json

@app.route('/')
@app.route('/index')
def index():

    if session:     #没有登录，跳到登录页面
        return render_template('info.html')
    else:
        return redirect("login")

@app.route('/login/', methods=['GET','POST'])
def login():
    db_fiels = app.config.get('DB_FIELDS')
    field = db_fiels.get('VERIFY_USER')

    if request.method == 'POST':
        '''获取表单数据，生成字典'''
        user = { k:v[0] for (k,v) in dict(request.form).items()}
        username = user['username']
        password = user['password']
        result = dbutils.verify_user('users', username,password,field)
        if result['code'] == 0 and result['msg']['status'] == 1:
            msg = u'用户已锁定'
            return render_template('login.html',msg=msg)
        elif result['code'] == 0:
            session['username'] = result['msg']['username']
            session['role'] = result['msg']['role']
            session['phone'] = result['msg']['phone']
            session['email'] = result['msg']['email']
            return redirect('index')
        else:
            msg = u'用户名密码错误'
            return render_template('login.html', msg=msg)

    else:
        return render_template('login.html')

@app.route('/create/', methods=['POST', 'GET'])
def create():
    db_fiels = app.config.get('DB_FIELDS')
    field = db_fiels.get('USER_FIELD')
    if request.method == 'POST':
        userdata = {k: v[0] for (k, v) in dict(request.form).items()}
        username = userdata['username']
        userdata['createtime'] = datetime.datetime.now()   #添加当前日期到表单字典
        result = dbutils.query('users',field) # 查询数据库返回的结果

        if result['code'] == 0 :
            user = [x['username'] for x in result['msg']]
            if username in user:
                msg_exist = u'用户已存在'
                return render_template('create.html', msg_exist=msg_exist)
        else:
            field = ["%s='%s'" % (k, v) for k, v in userdata.items()]
            msg_status = dbutils.create('users', field)
            return render_template('create.html',msg_status=msg_status)

    return render_template('create.html')

@app.route('/userlist/', methods=['POST', 'GET'])
def userlist():
    db_fiels = app.config.get('DB_FIELDS')
    all_field = db_fiels.get('USER_FIELD')
    result = dbutils.query('users', all_field)
    if result['code'] == 0:
        return render_template('userlist.html', msg=result['msg'])
    else:
        return render_template('userlsit.html', msg=result['errmsg'])



@app.route('/update/',methods=['POST', 'GET'])
def update():
    db_fiels = app.config.get('DB_FIELDS')
    field = db_fiels.get('USER_FIELD')
    id = request.args.get('id')

    if request.method == 'POST':
        pass
    else:

        result = dbutils.query('users', field, id)
        return render_template('userlist.html',result=result['msg'])
    return "d"


@app.route('/delete/',methods=['POST', 'GET'])
def delete():
    id = int(request.args.get('id'))
    dbutils.delete('users', id)
    return render_template('userlist.html')

@app.route('/logout/',methods=['POST', 'GET'])
def logout():
    if session:
        session.pop('role')
        session.pop('username')
        session.pop('email')
        session.pop('phone')
        return redirect('/login')
    return redirect('/login')
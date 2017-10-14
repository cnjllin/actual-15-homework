# Author: tailorYang
from flask import render_template,request,redirect,session
from app import app
import json,db,config,utils

@app.route('/')
@app.route('/index')
def index():
    if 'id' in session:
        res = db.select('user', id=session['id'])[0]
        user = {v: res[k] for k, v in enumerate(config.user_fields)}
        utils.writelog('user').info('"INFO: %s is Is visiting"'%user['username'])
        return render_template('/common/index.html',user=user,role=session['role'])
    return render_template('/common/login.html')

@app.route('/login/',methods=['post','get'])
def login():
    if request.method == 'GET':
        return render_template('/common/login.html')
    user_dict = {k:v[0] for k , v in dict(request.form).items()}
    if user_dict['username'] and user_dict['password']:
        res = db.select('user',**user_dict)[0]
        user = {v:res[k] for k,v in enumerate(config.user_fields)}
        if res:
            session['role'] = user['role']
            session['id'] = user['id']
            session['username'] = ['username']
            utils.writelog('user').info('"INFO: %s is login success"' %user['username'])
            return json.dumps({'code': '1', 'result':  'login success'})
        else:
            utils.writelog('user').error('"INFO: %s  login Failed"' %user_dict['username'])
            return json.dumps({'code': '0', 'result': 'name or password wrong'})
    else:
        utils.writelog('user').error('"INFO: %s  login Failed"' %user_dict['username'])
        return json.dump({'code':'0','result':'username or password not be null'})

@app.route('/useradd/',methods=['post','get'])
def useradd():
    if request.method == 'GET':
        return render_template('/user/add.html',role = session.get('role'))
    data = {k:v[0] for k,v in dict(request.form).items()}
    if db.add('user',data):
        return json.dumps({'code':1,'result':'add user success'})

@app.route('/userlist/')
def userlist():
    role = session.get('role')
    if role:
        res = db.select('user')
        users = [dict((v,user[k]) for k,v in enumerate(config.user_fields)) for user in res]
        return render_template("/user/userlist.html",users = users,role=role)

    else:
        res = db.select('user', id = session.get('id'))[0]
        user = {v: res[k] for k, v in enumerate(config.user_fields)}
        return render_template("/user/userinfo.html",user = user, role=role)

@app.route('/userinfo/')
def userinfo():
    if request.args.get('id'):
        user = db.select('user',id=request.args.get('id'))[0]
        user = {v: user[k] for k, v in enumerate(config.user_fields)}
        utils.writelog('user').info("INFO: {} is change {}'s info".format(session['username'],user['username']))
        return json.dumps({'result':user})
    else:
        role = session.get('role')
        res = db.select('user',id = session['id'])[0]
        user = {v: res[k] for k, v in enumerate(config.user_fields)}
        utils.writelog('user').info("INFO : %s is view his info "%user['username'])
        return render_template("/user/userinfo.html", user = user, role=role)

@app.route('/update/',methods=['GET','POST'])
def update():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    if data.get('newpassword'):
        conditions = ["password='%s'"%data.get('newpassword')]
    else:
        conditions = [ "%s='%s'" %(k,v) for k,v in data.items() if v !='id']
        session['role'] = data['role']
    db.update('user',conditions,data['id'])
    return json.dumps({'code':1,'result':'update completed!'})

@app.route('/delete/',methods=['post'])
def delete():
    db.delete('user',request.form.get('id'))
    return json.dumps({'code': 1, 'result': 'delete success!'})

@app.route('/logout/')
def loginout():
    utils.writelog('user').info('"INFO: %s logout"'%session['username'])
    if session:
        session.clear()
    return redirect('/login/')
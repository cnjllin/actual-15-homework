# Author: tailorYang
from flask import Flask,session,redirect,render_template,request
import json,utils
app = Flask(__name__)
fields = ['id', 'name', 'password', 'role', 'phone', 'job']

@app.route('/')
@app.route('/index')
def index():
    if 'name' in session:
        role = session.get('role')
        return render_template('index.html',role=role)
    else:
        return redirect('/login')

# 登录
@app.route('/login/',methods=['post','get'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = {k:v[0] for k,v in dict(request.form).items()}
        user = utils.get_one('user',fields,data)
        print(data)
        print(user)
        if not data.get('name') or not data.get('password'):
            errmsg = 'name or password not be null'
            return json.dumps({'code': '1', 'errmsg': errmsg})
        elif data['name'] == user['name'] and data['password'] == user['password'] :
            session['name'] = user['name']
            session['role'] = user['role']
            session['id'] = user['id']
            return json.dumps({'code': '0', 'result': 'login success'})
        else:
            errmsg = 'name or password wrong'
            return json.dumps({'code': '1', 'errmsg': errmsg})
# 添加用户
@app.route("/useradd/",methods=['GET','POST'])
def useradd():
    if request.method == 'GET':
        return render_template('add.html',role = session.get('role'))
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        l=[]
        for i in utils.list('user',fields):
            l.append(i['name'])
        if not data['name']:
            return json.dumps({'code':1,'errmsg':'name can not be null'})
        elif not data['password']:
            return json.dumps({'code':1,'errmsg':'password can not be null'})
        elif data['name'] in l:
            return json.dumps({'code': 1, 'errmsg': 'username is exist'})
        else:
            conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
            utils.add('user',conditions)
            return json.dumps({'code':0,'result':'add user success'})


# 用户列表
@app.route("/userlist/")
def userlist():
    role = session.get('role')
    if role == 1:
        users = utils.list('user',fields)
        return render_template("userlist.html",users = users,role = role)
    else:
        user = utils.list('users',fields,session.get('id'))
        return render_template("userself.html", user=user, role=role)

# 用户中心
@app.route('/userself/')
def userself():
    role = session.get('role')
    user = utils.list('user',fields,session.get('id'))
    return render_template("userself.html",user = user,role = role)

@app.route('/update_msg/')
def update_msg():
    id = request.args.get('id')
    user = utils.list('user',fields,id)
    if session.get('role') == 1:
        return json.dumps({'code':0,'result':user})
    else:
        return json.dumps({'code':2,'result':user})

#更新用户信息
@app.route('/update/',methods=['GET','POST'])
def update():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    user = [ "%s='%s'" %  (k,v) for k,v in data.items()]
    utils.update('user',user,data['id'])
    return json.dumps({'code':0,'result':'update completed!'})

# 更改用户密码
@app.route('/modpwd/',methods=['POST'])
def modpwd():
    data = {k: v[0] for k, v in dict(request.form).items()}
    if 'password' in data.keys():
        if not data['password'] or not data['newpassword'] or not data['renewpassword']:
            errmsg = 'password can not be null'
            return json.dumps({'code': '1', 'errmsg': errmsg})
    else:
        if not data['newpassword'] or not data['renewpassword']:
            errmsg = 'password can not be null'
            return json.dumps({'code': '1', 'errmsg': errmsg})
    try:
        condition = ["{}='{}'".format('password',v[0]) for k,v in data.items() if k == 'newpassword']
        id = session.get('id')
        if session.get('role') == 1:
            utils.update('user',condition,data['id'])
            return json.dumps({'code':'0','result':'modify completed!'})
        else:
            if data['password'] == utils.get_one('user',fields,data)['password']:
                utils.update('user', condition, data['id'])
                return json.dumps({'code': '0', 'result': 'modify completed!'})
            return json.dumps({'code': '1', 'errmsg': 'wrong old password'})
    except:
        errmsg = "modify failed"
        return json.dumps({'code': '1', 'errmsg': errmsg})

@app.route('/delete/',methods=['POST'])
def delete():
    id = request.form.get('id')
    utils.delete('user',id)
    return json.dumps({'code':0,'result':'delete success!'})

@app.route('/logout/')
def loginout():
    if session:
        session.pop('role')
        session.pop('name')
        session.pop('id')
        return redirect('/login')
    return redirect('/login')

if __name__ =="__main__":
    app.secret_key='QWEDCSXAWerere'
    app.run(debug=True)

